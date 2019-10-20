from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
from pymongo.operations import IndexModel

from devopstudio import config
from devopstudio.db import cusfields
from devopstudio.models import enums


mongo_config = config.MongoDBConfig()
connect(mongo_config.get_conn_str(config.OPSDB))


class SoftwareDataModel(EmbeddedMongoModel):
    os = fields.CharField()
    version = fields.CharField()
    image = fields.CharField()

    class Meta:
        indexes = [
            IndexModel('os'),
            IndexModel('version'),
            IndexModel('image'),
        ]


class NetworkObject(MongoModel):
    name = fields.CharField(primary_key=True, required=True)
    driver = fields.CharField(required=True)
    object_type = cusfields.EnumField(enums.ObjectType, required=True)
    management_ip = fields.CharField()
    children = fields.ListField(fields.ObjectIdField())
    software = fields.EmbeddedDocumentField(SoftwareDataModel)

    class Meta:
        indexes = [IndexModel('children')]


class InterfaceKey(EmbeddedMongoModel):
    no = fields.ReferenceField(NetworkObject)
    name = fields.CharField()

    class Meta:
        final = True


class NetworkInterfaceObject(MongoModel):
    key = fields.CharField()
    properties = fields.EmbeddedDocumentField(InterfaceKey, primary_key=True)


class NetworkObjectGroup(MongoModel):
    name = fields.CharField()
    group_type = cusfields.EnumField(enums.GroupType,
                                     default=enums.GroupType.TILE)
    exclusive = fields.BooleanField(default=False)
    members = fields.ListField(fields.ReferenceField(NetworkObject))


class TopologyLink(MongoModel):
    link_type = cusfields.EnumField(enums.LinkType)
    topology_type = cusfields.EnumField(enums.LinkType)
    no1 = fields.CharField()
    nio1 = fields.CharField()
    cp1 = fields.CharField()
    no2 = fields.CharField()
    nio2 = fields.CharField()
    cp2 = fields.CharField()


class NetworkRelationship(MongoModel):
    relationship_type = fields.CharField()
    source_no = fields.CharField()
    destination_no = fields.CharField()
