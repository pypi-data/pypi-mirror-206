import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Union

from hao.enums import OptionsMixin
from hao.uuid import UUID
from pydantic import BaseModel

_UUID = UUID()


def uuid():
    return str(_UUID.get())


class Permission(OptionsMixin, Enum):
    ADMIN = '管理员', 'admin'
    AI = '炼丹师', 'ai'


class User(BaseModel):
    name: str
    username: str
    password: Union[str, None] = None
    email: Union[str, None] = None
    permissions: List[str] = []
    timestamp: int = int(time.time())


@dataclass
class Task:
    name: str = field(default=None, )
    model: str = field(default=None)
    plm: str = field(default=None)
    dataset: str = field(default=None)
    created_by: str = field(default=None)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
