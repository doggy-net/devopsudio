from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
from pymongo.operations import IndexModel

from devopstudio import config
from devopstudio.common import enums
from devopstudio.db import cusfields


mongo_config = config.MongoDBConfig()
connect(mongo_config.get_conn_str(config.OPSDB))


class BasicDataModel(EmbeddedMongoModel):
    name = fields.CharField()


class NetworkObject(MongoModel):
    name = fields.CharField()
    children = fields.ListField(fields.ObjectIdField(),
                                mongo_name='chd')
    basic = fields.EmbeddedDocumentField(BasicDataModel)

    class Meta:
        indexes = IndexModel(['children'])


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
    topology_type = cusfields.EnumField(enums.LinkType,
                                        mongo_name='topo_type')
    no1 = fields.CharField()
    nio1 = fields.CharField()
    cp1 = fields.CharField()
    no2 = fields.CharField()
    nio2 = fields.CharField()
    cp2 = fields.CharField()


class NetworkRelationship(MongoModel):
    relationship_type = fields.CharField(mongo_name='rel_type')
    source_no = fields.CharField(mongo_name='src_no')
    destination_no = fields.CharField(mongo_name='dst_no')
