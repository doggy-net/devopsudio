from pymodm import connect

from devopstudio import config


mongo_config = config.MongoDBConfig()
connect(mongo_config.get_conn_str(config.DEVDB))
