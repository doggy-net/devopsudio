from pymodm import connect

import json


try:
    with open('config\\user_config.json') as user_config_file:
        user_config = json.loads(user_config_file.read())
        mongodb_servers = user_config.get('mongodb_servers')
        if mongodb_servers:
            servers = mongodb_servers.get('servers', [])
            for server in servers:
                connect(
                    'mongodb://%s/mydata?authSource=admin&authMechanism=SCRAM-SHA-1'
                    % server, username=mongodb_servers.get('username'),
                    password=mongodb_servers.get('password'))
except Exception as e:
    print(e)
