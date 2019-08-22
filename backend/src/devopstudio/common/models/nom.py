from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import fields, MongoModel, EmbeddedMongoModel
from models.enum_manager import Enum


MAX_LENGTH_CHAR = 128


class Property(EmbeddedMongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    no_id = fields.ObjectIdField()  # ID of associated Network Object
    var_type = fields.CharField(default=Enum.VariableType.STR)
    var_value = fields.CharField()


class Variable(MongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    no_id = fields.ObjectIdField()  # ID of associated Network Object
    var_type = fields.CharField(default=Enum.VariableType.STR)
    var_value = fields.CharField()


class ConnectionPoint(MongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    no_id = fields.ObjectIdField()  # ID of associated Network Object
    topo_type = fields.CharField(default=Enum.VariableType.STR)


class NetworkInterfaceObject(MongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    properties = fields.DictField()
    variables = fields.ListField(fields.ReferenceField(Variable), mongo_name='vars')
    connection_points = fields.ListField(
        fields.ReferenceField(Variable), mongo_name='cps')


class NetworkObject(MongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    properties = fields.DictField()
    variables = fields.ListField(fields.ReferenceField(Variable))
    connection_points = fields.ListField(
        fields.ReferenceField(Variable), mongo_name='cps')
    children = fields.ListField(fields.ObjectIdField(), mongo_name='chd')
    interfaces = fields.ListField(fields.ReferenceField(
        NetworkInterfaceObject), mongo_name='intfs')


class NetworkObjectGroup(MongoModel):
    name = fields.CharField(max_length=MAX_LENGTH_CHAR)
    group_type = fields.CharField(default=Enum.GroupType.TILE)
    exclusive = fields.BooleanField(default=False)
    members = fields.ListField(fields.ReferenceField(NetworkObject))


class NetworkLink(MongoModel):
    link_type = fields.CharField()
    cp1 = fields.ReferenceField(ConnectionPoint)
    no_name1 = fields.CharField()
    nio_name1 = fields.CharField()
    cp2 = fields.ReferenceField(ConnectionPoint)
    no_name2 = fields.CharField()
    nio_name2 = fields.CharField()


class NetworkRelationship(MongoModel):
    relationship_type = fields.CharField()
    source_no = fields.ReferenceField(NetworkObject)
    source_no_name = fields.CharField()
    destination_no = fields.ReferenceField(NetworkObject)
    destination_no_name = fields.CharField()
