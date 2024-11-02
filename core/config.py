import os
from core.env_config import config

DATABASES = {
    'type': os.environ.get('type', config["DatabaseConfig"]['DB_TYPE']),
    'database': os.environ.get('database', config["DatabaseConfig"]['DATABASE']),
    'username': os.environ.get('username', config["DatabaseConfig"]['USERNAME']),
    'password': os.environ.get('password', config["DatabaseConfig"]['PASSWORD']),
    'host': os.environ.get('host', config["DatabaseConfig"]['HOST']),
    'port': os.environ.get('port', config["DatabaseConfig"]['DB_PORT']),
}

_DATABASES = {
    'type': '',
    'username': '',
    'password': '',
    'host': '',
    'port': '',
    'database': '',
}
# ~~~~~ APP ~~~~~
PROJECT_NAME = os.getenv('PROJECT_NAME', 'Employee Management')


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ('TRUE', '1')
    return result

# ~~~~~ TEST ~~~~~

TEST_RUN = getenv_boolean('TEST_RUN', False)

# ~~~~~ SECRET ~~~~~
SECRET_KEY = os.getenv('SECRET_KEY', 'cuerno de unicornio :D')

if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)


class Config:
    LIMIT = 3