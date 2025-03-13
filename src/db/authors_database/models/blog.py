from tortoise import fields
from tortoise.models import Model

class Blog(Model):
  id = fields.IntField(pk=True)
  owner = fields.ForeignKeyField("authors_database.User", to_field="id", on_delete=fields.CASCADE)
  name = fields.CharField(max_length=100)
  description = fields.CharField(max_length=255)

  class Meta:
    table = "blogs"