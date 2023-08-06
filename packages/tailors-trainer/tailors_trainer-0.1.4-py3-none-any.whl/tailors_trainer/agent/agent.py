import hao

LOGGER = hao.logs.get_logger(__name__)


def run():
    try:
        manager_endpoint = hao.envs.get_str('tailors_manager')
        if manager_endpoint is None or not manager_endpoint.startswith('http'):
            LOGGER.error(f"env: 'tailors_manager' is required.")
            return

    except KeyboardInterrupt:
        print('[ctrl-c]')
    except Exception as err:
        LOGGER.exception(err)


if __name__ == '__main__':
    run()
