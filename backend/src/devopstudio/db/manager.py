from enum import Enum as enum_class

from pymodm import connect, fields, MongoModel

from devopstudio import config
from devopstudio.common.utils.class_helper import get_local_classes


mongo_config = config.MongoDBConfig()
mongo_config.get_conn_str(config.DEVDB)


class Enum(MongoModel):
    name = fields.CharField(primary_key=True)
    enums = fields.DictField()

    class Meta:
        final = True


def save_to_db():
    for local_cls in get_local_classes(__name__, enum_class):
        Enum(name=local_cls.__name__, enums={e.name: e.value for e in local_cls}).save()


if __name__ == '__main__':
    save_to_db()
