from celery import Celery

from devopstudio.config import MongoDBConfig, MQConfig
from . import config


mq_config = MQConfig()
amqp_conn_str = mq_config.get_conn_str()
db_config = MongoDBConfig()
db_conn_str = db_config.get_conn_str('task')

app = Celery(__name__,
             broker=amqp_conn_str,
             backend=f'{db_conn_str}',
             include='devopstudio.worker.tasks')
app.config_from_object(config)
