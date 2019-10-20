from pymodm import fields, MongoModel


class Enum(MongoModel):
    name = fields.CharField(primary_key=True)
    enums = fields.DictField()

    class Meta:
        final = True


class OneInstanceTask(MongoModel):
    name = fields.CharField(primary_key=True)
    task_id = fields.CharField()


class Disovery(MongoModel):
    name = fields.CharField(primary_key=True)
    task_id = fields.CharField()
