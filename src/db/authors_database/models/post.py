from tortoise import fields
from tortoise.models import Model

class Post(Model):
  id = fields.IntField(pk=True)
  header = fields.CharField(max_length=100)
  text = fields.CharField(max_length=255)
  author = fields.ForeignKeyField("authors_database.User", to_field="id", on_delete=fields.CASCADE)
  blog = fields.ForeignKeyField("authors_database.Blog", to_field="id", on_delete=fields.CASCADE)

  class Meta:
    table = "posts"