from tortoise import fields
from tortoise.models import Model


class SpaceType(Model):
  id = fields.IntField(pk=True)
  name = fields.CharField(max_length=50)

  class Meta:
    table = "space_type"

class EventType(Model):
  id = fields.IntField(pk=True)
  name = fields.CharField(max_length=50)

  class Meta:
    table = "event_type"