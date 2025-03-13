from tortoise import fields
from tortoise.models import Model

class Log(Model):
  id = fields.IntField(pk=True)
  datetime = fields.DatetimeField(auto_now_add=True)  # При создании лога время можно не указывать
  user_id = fields.IntField()
  space_type = fields.ForeignKeyField("logs_database.SpaceType", to_field="id", on_delete=fields.CASCADE)
  event_type = fields.ForeignKeyField("logs_database.EventType", to_field="id", on_delete=fields.CASCADE) 

  class Meta:
    table = "logs"