import json
from pathlib import Path


ADMINDB = 'admin'
DEVDB = 'dev'
OPSDB = 'ops'


_config = {
    'amqp': {
        'host': 'localhost',
        'port': 5672,
        'username': '',
        'password': '',
    },
    'mongodb': {
        'host': 'localhost',
        'username': '',
        'password': '',
        'ssl': False,
        'authMechanism': 'SCRAM-SHA-256',
    },
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'username': '',
        'password': '',
    }
}

_user_config = {}
_cwd = Path(__file__).parent
try:
    with open(_cwd / Path('config.json')) as uf:
        _user_config = json.loads(uf.read())
except Exception:
    pass


class Config:

    def __init__(self):
        self._config = _config
        print(_user_config, self._config)
        self._config.update(_user_config)
        print(self._config)

    def get_property(self, *keys, default=None):
        result = self._config
        for key in keys:
            if key in result:
                result = result[key]
            else:
                return default
        return default


class MongoDBConfig(Config):

    @property
    def host(self):
        return self.get_property('mongodb', 'host')

    @property
    def username(self):
        return self.get_property('mongodb', 'username')

    @property
    def password(self):
        return self.get_property('mongodb', 'password')

    @property
    def ssl(self):
        return self.get_property('mongodb', 'ssl')

    def get_conn_str(self, database):
        # mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database][?options]]
        if self.username and self.password:
            authen_str = f'{self.username}:{self.password}@'
        else:
            authen_str = ''
        if self.ssl:
            ssl_str = '&ssl=true'
        else:
            ssl_str = ''
        return f'mongodb://{authen_str}{self.host}/{database}?authSource=admin{ssl_str}'
