import pytest
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        '--testbed',
        action='store',
        help='Environment to Test Against'
    )


@pytest.fixture(scope='session')
def get_env_cli(request):
    return request.config.getoption('--testbed')


@pytest.fixture(scope='session')
def app_config(get_env_cli):
    return Config(get_env_cli).my_env


# def pytest_configure(config):
#     config.addinivalue_line("markers", "Mark test as testbed as applicable")
#
#
# def pytest_load_initial_conftests(args):
#     args[:] = ["-m", get_env_cli] + args
