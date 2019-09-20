from enum import Enum

from pymodm import fields, validators


class EnumField(fields.MongoBaseField):
    """A field that stores a Python enum."""

    def __init__(self, enum_type, verbose_name=None, mongo_name=None, **kwargs):
        """
        :parameters:
          - `enum_type`: The type of this enum field.
          - `verbose_name`: A human-readable name for the field.
          - `mongo_name`: The name of this field when stored in MongoDB.

        .. seealso:: constructor for
                     :class:`~pymodm.base.fields.MongoBaseField`
        """
        if not issubclass(enum_type, Enum):
            raise TypeError(f"'enum_type' must be sub class of 'Enum'")
        self._enum_type = enum_type
        super().__init__(verbose_name=verbose_name,
                         mongo_name=mongo_name,
                         **kwargs)
        self.validators.append(
            validators.together(
                validators.validator_for_type(enum_type),
                validators.validator_for_func(enum_type)))

    def to_python(self, value):
        return self._enum_type(value)

    def to_mongo(self, value):
        return value.value
