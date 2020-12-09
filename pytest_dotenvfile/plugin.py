import os

from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--env-file",
        type=str,
        dest="env_file",
        help="The path to the env file to load",
    )

    parser.addoption(
        "--override-system-env",
        type=bool,
        dest="override_system_env",
        help="Whether dotenv should override existing system variables",
    )


def load_env_file(env_file, override=False):
    if os.path.isfile(env_file):
        load_dotenv(env_file, override=override)
    else:
        raise FileNotFoundError()


def pytest_sessionstart(session):
    config = session.config

    env_file = config.getoption("env_file", default=None)
    override_system_env = config.getoption("override_system_env", default=False)

    if env_file is not None:
        load_env_file(env_file, override_system_env)
