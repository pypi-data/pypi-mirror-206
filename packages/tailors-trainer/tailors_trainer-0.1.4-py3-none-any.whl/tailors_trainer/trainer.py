# -*- coding: utf-8 -*-
import collections
import importlib
import os
from datetime import datetime
from types import SimpleNamespace
from typing import Optional

import hao
import pandas as pd
import torch
import torchinfo
from hao.namespaces import attr, from_args
from peft import PeftType, TaskType, get_peft_config, get_peft_model_state_dict, set_peft_model_state_dict
from tailors import append_batch, losses, move_to_device, set_seed
from tailors.exceptions import TailorsError
from tailors.metrics import classification_metrics
from tailors.models import Tailors
from torch.nn.parallel import DistributedDataParallel
from torch.utils.data.dataloader import DataLoader
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from tailors_trainer import callbacks, model_size, optimizers, pefts, schedulers
from tailors_trainer.data import DatasetConf, TailorDataset
from tailors_trainer.exceptions import StopTailorsTrainer, TailorsTrainerError

LOGGER = hao.logs.get_logger('trainer')


@from_args
class TrainConf:
    """Hyperparams"""
    model: str = attr(str, required=True)
    dataset: str = attr(str, required=True)
    seed = attr(int, default=1000)
    max_epochs: int = attr(int, default=50)
    loss = attr(str, choices=tuple(losses.LOSSES))
    lr: float = attr(float, default=1e-4)
    optimizer = attr(str, choices=tuple(optimizers.OPTIMIZERS), default=list(optimizers.OPTIMIZERS)[0])
    weight_decay: float = attr(float, default=1e-2)
    scheduler: str = attr(str, choices=tuple(schedulers.SCHEDULERS), default=list(schedulers.SCHEDULERS)[0])
    clip_norm: float = attr(float, default=1.0, help='clip grad norm for NLP tasks, generally: 1.0')
    amp: bool = attr(bool, default=False)
    accumulation: int = attr(int, default=1)
    peft: str = attr(str, choices=tuple(t.value.lower() for t in PeftType), default=None)
    peft_task_type: str = attr(str, choices=tuple(t.value.lower() for t in TaskType))


@from_args
class TrainerConf:
    """Non-hyperparams"""
    exp: str = attr(str, required=True)
    gpus: str = attr(str, help='gpu indices separated by comma, no spaces')
    logger: str = attr(str, default='tensorboard')
    log_model_summary: bool = attr(bool, default=True)
    log_model_depth: int = attr(int, default=3)
    resume_from: str = attr(str)
    early_stop_patience: int = attr(int, default=5)
    track_dynamics: bool = attr(bool, default=False)
    checkpoint_name: str = attr(str, default='{model}-{dataset}-{exp}-{ts}-epoch={epoch}-val_loss={loss_val}-f1={f1}.ckpt')
    save_top_n: int = attr(int, default=1)
    save_last: bool = attr(bool, default=False)


class TrainerState:
    def __init__(self) -> None:
        self.ts = datetime.now().strftime('%y%m%d-%H%M')
        self.bz = 0
        self.steps_per_epoch = {}
        self.step = 0
        self.epoch = -1
        self.batch_id = -1
        self.val_losses = []
        self.metrics = {}
        self.reports = {}
        self._ckpts = SimpleNamespace(top_n=[], last=None, should_save=False, new_path=None)
        self._resume_state_dict = None

    def set_metric(self, key, value):
        self.metrics[key] = value
        if key == 'loss/val':
            self.val_losses.append(value)

    def set_metrics(self, metrics: dict):
        for k, v in metrics.items():
            if 'report' in k.lower():
                self.reports[k] = v
            else:
                self.set_metric(k, v)

    def state_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}

    def load_state_dict(self, state_dict):
        for k, v in state_dict.items():
            setattr(self, k, v)


class Trainer:
    def __init__(self, trainer_conf: Optional[TrainerConf] = None, train_conf: Optional[TrainConf] = None) -> None:
        super().__init__()
        self.trainer_conf = trainer_conf or TrainerConf()
        self.train_conf = train_conf or TrainConf()
        LOGGER.info(self.trainer_conf)
        LOGGER.info(self.train_conf)
        self.device, self.rank, self.world_size = self.check_devices()
        self.state = TrainerState()
        self.exp_dir = f"data/exps/{self.train_conf.model}/{self.train_conf.dataset}/{self.trainer_conf.exp}-{self.state.ts}"
        self.callback_handler = callbacks.CallbackHandler(self.train_conf, self.trainer_conf, self.state, self.exp_dir)
        self.load_resume_from_state_dict()

        set_seed(self.train_conf.seed)
        self.model: Tailors = self.get_model()
        self.dataloaders, self.state.steps_per_epoch = self.get_dataloaders()

        self.criteria = losses.get(self.train_conf.loss) if self.train_conf.loss else None
        self.scaler = self.get_scaler()
        self.optimizer = self.get_optimizer()
        self.scheduler = self.get_scheduler()

        self.validate()

        self.go_thru_resume_from_state_dict()
        self.log_model_summary()

    def check_devices(self):
        rank = 0
        if self.trainer_conf.gpus:
            gpus = [gpu for gpu in self.trainer_conf.gpus.split(',') if gpu and gpu.isdigit() and 0 <= int(gpu)]
            cuda_visible_devices = ','.join(gpus)
            os.environ['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices
            LOGGER.info(f"CUDA_VISIBLE_DEVICES={cuda_visible_devices}")

            is_cuda_available, n_devices = torch.cuda.is_available(), torch.cuda.device_count()
            if is_cuda_available and n_devices > 0:
                device = torch.device(f"cuda:{rank}")
                LOGGER.info(f"[device] {device}, cuda available: {is_cuda_available}, device count: {n_devices}")
                return device, rank, n_devices
        else:
            is_cuda_available, n_devices = torch.cuda.is_available(), torch.cuda.device_count()

        device = torch.device('cpu')
        LOGGER.info(f"[device] {device}, cuda available: {is_cuda_available}, device count: {n_devices}")
        return device, rank, n_devices

    def load_resume_from_state_dict(self):
        checkpoint_path = hao.paths.get(self.trainer_conf.resume_from)
        if checkpoint_path is None or not os.path.isfile(checkpoint_path):
            return
        LOGGER.info(f"[resume from] {checkpoint_path}")
        self.state._resume_state_dict = torch.load(checkpoint_path)

    def validate(self):
        if self.criteria is None and not hasattr(self.model, 'compute_loss'):
            raise TailorsTrainerError('Expecting either `--loss=xxx` or `compute_losss()` method')

    def go_thru_resume_from_state_dict(self):
        if self.state._resume_state_dict is None:
            return
        for key, attri in (
            ('state', 'state'),
            ('state_dict', 'model'),
            ('scaler_state_dict', 'scaler'),
            ('optimizer_state_dict', 'optimizer'),
            ('scheduler_state_dict', 'scheduler'),
        ):
            if (m := getattr(self, attri, None)) is None or (state_dict := self.state._resume_state_dict.get(key)) is None:
                continue
            m.load_state_dict(state_dict)

        state_dict = state_dict.get('state_dict')
        if (peft_config := self.state._resume_state_dict.get('peft_config')) is None:
            self.model.load_state_dict(state_dict)
        else:
            self.model.peft_config = get_peft_config(peft_config)
            set_peft_model_state_dict(self.model, state_dict)
        self.state._resume_state_dict = None

    def get_model(self) -> Tailors:
        model_fqn = self.train_conf.model
        module_name, _, model_class_name = model_fqn.rpartition('.')
        module = importlib.import_module(module_name)
        model_class = getattr(module, model_class_name)

        if self.state._resume_state_dict is not None:
            model_conf = self.state._resume_state_dict.get('model_conf')
        else:
            model_conf_class = getattr(module, f"{model_class_name}Conf")
            meta = hao.config.get(f"datasets.{self.train_conf.dataset}", config='tailors.yml').get('meta')
            if meta is None or not isinstance(meta, dict) or len(meta) == 0:
                raise TailorsError(f"expecting `meta` dict in corpora.{self.train_conf.dataset}, in `tailors.yml`")
            model_conf = model_conf_class(meta=meta)
        LOGGER.info(model_conf)
        model = model_class(model_conf)
        model = pefts.peftify(model, self.train_conf.peft, self.train_conf.peft_task_type)
        model.use_device(self.device)

        if self.world_size > 1:
            model = DistributedDataParallel(model, device_ids=[self.rank], output_device=self.rank)
        return model

    def get_dataloaders(self):
        datasets = hao.config.get(f"datasets.{self.train_conf.dataset}", config='tailors.yml').get('datasets')
        dataset_conf = DatasetConf()
        LOGGER.info(dataset_conf)
        self.state.bz = dataset_conf.bz
        dataloaders = {
            split: TailorDataset(self.model.io, self.train_conf.dataset, split, files, dataset_conf).dataloader()
            for split, files in datasets.items()
        }
        steps_per_epochs = {split: len(dataloader) for split, dataloader in dataloaders.items()}
        return dataloaders, steps_per_epochs

    def get_scaler(self):
        return torch.cuda.amp.GradScaler() if self.train_conf.amp else None

    def get_optimizer(self):
        def get_bucket(name):
            for key in rates:
                if name.startswith(key):
                    return key
            return 'default'

        rates = {name: f.apply(self.train_conf.lr) for name, f in self.model.lr_factors().items()}

        no_decay = ['bias', 'gamma', 'beta', 'LayerNorm.weight', 'LayerNorm.bias']
        no_decay_suffix = '_no_decay'
        groups_default, groups_named, group_meta = collections.defaultdict(list), collections.defaultdict(list), {}
        for n, p in self.model.named_parameters():
            if len(p) == 0:
                continue
            bucket = get_bucket(n)
            is_no_decay = any(nd in n for nd in no_decay)
            groups = groups_default if bucket == 'default' else groups_named
            key = f"{bucket}{no_decay_suffix}" if is_no_decay else bucket
            groups[key].append(p)
            if key not in group_meta:
                weight_decay = 0 if is_no_decay else self.train_conf.weight_decay
                lr = rates.get(bucket, self.train_conf.lr)
                group_meta[key] = {'weight_decay': weight_decay, 'lr': lr, 'name': key}

        grouped_parameters = []
        for key, params in groups_default.items():
            grouped_parameters.append({'params': params, **group_meta.get(key)})
        for key, params in groups_named.items():
            grouped_parameters.append({'params': params, **group_meta.get(key)})
        return optimizers.get(self.train_conf.optimizer, grouped_parameters)

    def get_scheduler(self):
        return schedulers.get(self.train_conf.scheduler, self.optimizer, steps_per_epoch=self.state.steps_per_epoch.get('train'))

    def log_model_summary(self):
        if self.trainer_conf.log_model_summary:
            summary = torchinfo.summary(
                self.model,
                col_names=('num_params', 'trainable'),
                mode='train',
                row_settings=('ascii_only',),
                depth=self.trainer_conf.log_model_depth,
                verbose=0,
            )
            LOGGER.info(f"[summary] {self.train_conf.model}\n{summary}")
            LOGGER.info(f"estimated size: {model_size(self.model)}")

    def get_lr(self):
        if hasattr(self.scheduler, 'get_lr'):
            return self.scheduler.get_lr()
        return self.get_lrs()[0]

    def get_lrs(self):
        return [group["lr"] for group in self.optimizer.param_groups]

    def fit(self):
        LOGGER.info('[fit] start')
        sw = hao.stopwatch.Stopwatch()
        self.prepare_fit()
        self.callback_handler.on_fit_start()
        try:
            dataloader_train, dataloader_val = self.dataloaders.get('train'), self.dataloaders.get('val')
            for epoch in range(self.state.epoch + 1, self.train_conf.max_epochs):
                LOGGER.info(f"[epoch {epoch}] start")
                self.state.epoch = epoch
                self.callback_handler.on_epoch_start()
                self.train_epoch(epoch, dataloader_train)
                self.val_epoch(epoch, dataloader_val)
                self.lr_scheduler_step()
                self.log_metrics()
                self.callback_handler.on_epoch_end()
                self.save_if_should()
                LOGGER.info(f"[epoch {epoch}] end, took {sw.lap()}")
        except StopTailorsTrainer:
            pass
        finally:
            self.callback_handler.on_fit_end()
            self.save_model()
            LOGGER.info(f"[fit] end, took: {sw.took()}")

    def prepare_fit(self):
        set_seed(self.train_conf.seed)

        # ignore tokenizer fork warning
        os.environ['TOKENIZERS_PARALLELISM'] = 'false'

        # RuntimeError: unable to open shared memory object
        torch.multiprocessing.set_sharing_strategy('file_system')

    def train_epoch(self, epoch: int, dataloader: DataLoader):
        self.model.train()
        self.callback_handler.on_train_epoch_start()
        losses, dynamics = [], collections.defaultdict(list)
        acmu = max(1, self.train_conf.accumulation)
        with logging_redirect_tqdm():
            batches = tqdm(dataloader, desc=f"[epoch {epoch}] training  ", ascii=' ━', colour='blue')
            for batch_id, batch in enumerate(batches):
                self.state.batch_id = batch_id
                self.state.step += acmu
                self.callback_handler.on_train_batch_start()

                batch = move_to_device(batch, self.model.device)
                is_optimizer_step = acmu == 1 or self.state.step % acmu == 0

                if self.scaler:
                    with torch.cuda.amp.autocast(True):
                        encoded = self.model.encode(batch.features)
                        decoded = self.model.decode(encoded)
                        loss = self.compute_loss(encoded, decoded, batch.target)
                        loss = loss / acmu

                    self.scaler.scale(loss).backward()
                    loss = loss.item()
                    losses.append(loss)
                    if self.train_conf.clip_norm > 0:
                        self.scaler.unscale_(self.optimizer)
                        torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.train_conf.clip_norm)
                    if is_optimizer_step:
                        self.scaler.step(self.optimizer)
                        self.scaler.update()
                        self.optimizer.zero_grad(set_to_none=True)
                        batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})

                else:
                    encoded = self.model.encode(batch.features)
                    decoded = self.model.decode(encoded)
                    loss = self.compute_loss(encoded, decoded, batch.target)
                    loss = loss / acmu
                    loss.backward()
                    loss = loss.item()
                    losses.append(loss)

                    if self.train_conf.clip_norm > 0:
                        torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.train_conf.clip_norm)
                    if is_optimizer_step:
                        self.optimizer.step()
                        self.optimizer.zero_grad(set_to_none=True)
                        batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})
                self.state.set_metric('loss/batch', loss)

                if self.trainer_conf.track_dynamics is True:
                    logits = encoded[0] if isinstance(encoded, tuple) else encoded
                    logits = logits.detach().cpu().tolist()
                    target = batch.target.detach().cpu().tolist()
                    for guid, logits, gold in zip(batch.idx, logits, target):
                        dynamics['epoch'].append(epoch)
                        dynamics['guid'].append(guid)
                        dynamics['logits'].append(logits)
                        dynamics['gold'].append(gold)

                self.callback_handler.on_train_batch_end()

        self.state.set_metric('loss/train', sum(losses) / len(losses))
        self.save_dynamics(epoch, dynamics)
        self.callback_handler.on_train_epoch_end()

    def val_epoch(self, epoch: int, dataloader: DataLoader):
        self.model.eval()
        self.callback_handler.on_val_epoch_start()
        losses, encodeds, decodeds, targets = [], [], [], []
        with logging_redirect_tqdm(), torch.no_grad():
            batches = tqdm(dataloader, desc=f"[epoch {epoch}] validating", ascii=' ━', colour='green')
            for batch_id, batch in enumerate(batches):
                self.state.batch_id = batch_id
                self.callback_handler.on_eval_batch_start()

                batch = move_to_device(batch, self.model.device)
                encoded = self.model.encode(batch.features)
                decoded = self.model.decode(encoded)
                loss = self.compute_loss(encoded, decoded, batch.target)
                loss = loss.item()
                losses.append(loss)
                append_batch(encodeds, encoded)
                append_batch(decodeds, decoded)
                append_batch(targets, batch.target)
                batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})

                if (on_eval_batch_end := getattr(self.model, 'on_eval_batch_end', None)) is not None:
                    on_eval_batch_end(encoded, decoded, batch.target)

                self.callback_handler.on_eval_batch_end()

        self.state.set_metric('loss/val', sum(losses) / len(losses))
        self.compute_metrics(encodeds, decodeds, targets)
        self.callback_handler.on_val_epoch_end()

    def compute_loss(self, encoded, decoded, target):
        if (criteria := getattr(self.model, 'compute_loss', None)) is not None:
            return criteria(encoded, decoded, target)
        y_pred = encoded[0] if isinstance(encoded, tuple) else encoded
        y_true = target[0] if isinstance(target, tuple) else target
        return self.criteria(y_pred, y_true)

    def compute_metrics(self, encodeds, decodeds, targets):
        if (metrics_fn := getattr(self.model, 'compute_metrics', None)) is not None:
            metrics = metrics_fn(encodeds, decodeds, targets)
        else:
            metrics = classification_metrics.calculate(targets[0], decodeds[0], self.model.io.tags.id2tag)
        self.state.set_metrics(metrics)

    def lr_scheduler_step(self):
        scheduler_args = {'metrics': self.state.metrics.get('loss/val'), 'epoch': self.state.epoch}
        hao.invoker.invoke(self.scheduler.step, **scheduler_args)

        # get the new lrs
        lrs = self.get_lrs()
        self.state.set_metrics({'lr': lrs[0], 'lrs': lrs})

    def log_metrics(self):
        width = max(len(k) for k, _ in self.state.metrics.items()) + 1
        metrics = '\n'.join([f"\t{k: <{width}}: {v}" for k, v in self.state.metrics.items()])
        LOGGER.info(f"{' metrics '.center(50, '━')}\n{metrics}")
        for k, v in self.state.reports.items():
            LOGGER.info(f"{f' {k} '.center(50, '━')}\n{v}")

    def save_dynamics(self, epoch: int, dynamics: dict):
        if len(dynamics) == 0:
            return
        path = f"{self.exp_dir}/dynamics-{epoch:0>2}.pkl"
        hao.paths.make_parent_dirs(hao.paths.get(path))
        df = pd.DataFrame(dynamics)
        df.to_pickle(path)

    def save_if_should(self):
        if self.state._ckpts.should_save:
            self.state._ckpts.path_new = self.save()
            self.callback_handler.on_save_checkpoint()
            self.state._ckpts.should_save = False

    def save(self, name: Optional[str] = None):
        state_dicts = {
            'train_conf': self.train_conf,
            'model_conf': self.model.model_conf,
            'optimizer_state_dict': self.optimizer.state_dict(),
            'scheduler_state_dict': self.scheduler.state_dict(),
        }
        if (peft_config := getattr(self.model, 'peft_config', None)) is None:
            self.model.on_save_checkpoint()
            state_dicts['state_dict'] = self.model.state_dict()
        else:
            state_dicts['state_dict'] = get_peft_model_state_dict(self.model)
            state_dicts['peft_config'] = {**peft_config.__dict__ , 'inference_mode': True}

        if self.scaler:
            state_dicts['scaler_state_dict'] = self.scaler.state_dict()
        params = {
            'model': self.train_conf.model,
            'dataset': self.train_conf.dataset,
            'exp': self.trainer_conf.exp or 'na',
            'epoch': self.state.epoch,
            'ts': self.state.ts,
            **{k.replace('/', '_'): f"{v:.4f}" for k, v in self.state.metrics.items() if isinstance(v, (str, int, float, bool))},
        }
        checkpoint_name = name or self.trainer_conf.checkpoint_name
        filename = checkpoint_name.format(**params)
        filepath = f"data/checkpoints/{filename}"
        fullpath = hao.paths.get(filepath)
        hao.paths.make_parent_dirs(fullpath)
        torch.save(state_dicts, fullpath)
        LOGGER.debug(f"saved checkpoint: {filepath}")
        return filepath

    def save_model(self):
        if self.state.epoch <= 0 or len(self.state._ckpts.top_n) == 0:
            return
        checkpoint_path = self.state._ckpts.top_n[0][1]
        if not os.path.isfile(checkpoint_path):
            return
        filebase, _ = os.path.splitext(os.path.basename(checkpoint_path))
        filepath = f"data/model/{filebase}.bin"
        fullpath = hao.paths.get(filepath)
        if (peft_config := getattr(self.model, 'peft_config', None)) is None:
            self.model.export_to_model(fullpath)
        else:
            state_dicts = {
                'model_conf': self.model.model_conf,
                'state_dict': get_peft_model_state_dict(self.model),
                'peft_config': {**peft_config.__dict__ , 'inference_mode': True},
            }
            hao.paths.make_parent_dirs(fullpath)
            torch.save(state_dicts, fullpath)
        LOGGER.info(f"saved model: {filepath}")
