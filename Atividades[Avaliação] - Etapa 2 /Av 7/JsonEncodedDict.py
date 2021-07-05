import json
import sqlalchemy as sqla
from sqlalchemy.ext import mutable

class JsonEncodedDict(sqla.TypeDecorator):
  """Enables JSON storage by encoding and decoding on the fly."""
  impl = sqla.String

  def process_bind_param(self, value, dialect):
    return simplejson.dumps(value)

  def process_result_value(self, value, dialect):
    return simplejson.loads(value)

mutable.MutableDict.associate_with(JsonEncodedDict)
