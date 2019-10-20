import json
from pathlib import Path

from devopstudio.utils.mixin import dict_mixin


SYSDB = 'sys'
DEVDB = 'dev'
OPSDB = 'ops'


_config = {
    'amqp': {
        'host': 'localhost',
        'username': 'guest',
        'password': 'guest',
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
        dict_mixin(self._config, _user_config)

    def get_property(self, *keys, default=None):
        result = self._config
        for key in keys:
            if key in result:
                result = result[key]
            else:
                return default
        return result


class MQConfig(Config):

    @property
    def host(self):
        return self.get_property('amqp', 'host')

    @property
    def username(self):
        return self.get_property('amqp', 'username')

    @property
    def password(self):
        return self.get_property('amqp', 'password')

    # amqp_URI       = "amqp://" amqp_authority [ "/" vhost ]
    # amqp_authority = [ amqp_userinfo "@" ] host [ ":" port ]
    # amqp_userinfo  = username [ ":" password ]
    # username       = *( unreserved / pct-encoded / sub-delims )
    # password       = *( unreserved / pct-encoded / sub-delims )
    # vhost          = segment
    def get_conn_str(self):
        if self.username and self.password:
            authen_str = f'{self.username}:{self.password}@'
        else:
            authen_str = ''
        return f'amqp://{authen_str}{self.host}/'


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

    @property
    def auth_mechanism(self):
        return self.get_property('mongodb', 'authMechanism')

    # mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database][?options]]
    # https://docs.mongodb.com/manual/reference/connection-string/#connections-connection-options
    def get_conn_str(self, database):
        if self.username and self.password:
            authen_str = f'{self.username}:{self.password}@'
        else:
            authen_str = ''
        if self.ssl:
            ssl_str = '&ssl=true'
        else:
            ssl_str = ''
        if self.ssl:
            ssl_str = '&ssl=true'
        else:
            ssl_str = ''
        if self.auth_mechanism:
            auth_mechanism_str = f'&authMechanism={self.auth_mechanism}'
        else:
            auth_mechanism_str = ''
        return f'mongodb://{authen_str}{self.host}/{database}?authSource=admin{ssl_str}'
