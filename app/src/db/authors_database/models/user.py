from tortoise import fields
from tortoise.models import Model

class User(Model):
  id = fields.IntField(pk=True)
  email = fields.CharField(max_length=255, unique=True)
  login = fields.CharField(max_length=255, unique=True)

  class Meta:
    table = "users"