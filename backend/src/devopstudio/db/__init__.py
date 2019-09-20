from pymodm import connect

from devopstudio import config
from devopstudio.common.utils.class_helper import get_local_classes


mongo_config = config.MongoDBConfig()
connect(mongo_config.get_conn_str(config.DEVDB))
