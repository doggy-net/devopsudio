from pymodm import EmbeddedMongoModel, MongoModel, fields

from devopstudio.db import cusfields
from devopstudio.models.enums import ExplorerNodeType


class OneInstanceTask(MongoModel):
    name = fields.CharField(primary_key=True)
    task_id = fields.CharField()


class Disovery(MongoModel):
    name = fields.CharField(primary_key=True)
    task_id = fields.CharField()


class ExplorerNode(EmbeddedMongoModel):
    name = fields.CharField(required=True)
    type = cusfields.EnumField(ExplorerNodeType, required=True)
    icon = fields.CharField(blank=True)
    path = fields.CharField()
    level = fields.IntegerField(default=0)
    parent = fields.CharField(blank=True)
    children = fields.ListField(blank=True)


class Explorer(MongoModel):
    name = fields.CharField(primary_key=True)
    nodes = fields.EmbeddedDocumentListField(ExplorerNode, blank=True)
