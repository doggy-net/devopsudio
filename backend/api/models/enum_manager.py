from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
import models.db_manager

import json


class Enum(MongoModel):
    name = fields.CharField(primary_key=True)
    enums = fields.DictField()

    class Meta:
        final = True


try:
    for enum_doc in Enum.objects:
        enum_class = type(enum_doc.name, (object, ), enum_doc.enums)
        setattr(Enum, enum_doc.name, enum_class)
except Exception as e:
    print(e)
