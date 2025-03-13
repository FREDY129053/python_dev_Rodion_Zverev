# Добавляем таблицу comments для подсчета комментариев у поста
from tortoise import fields
from tortoise.models import Model

class Comment(Model):
  id = fields.IntField(pk=True)
  text = fields.CharField(max_length=255)
  author = fields.ForeignKeyField("authors_database.User", related_name="comments", to_field="id", on_delete=fields.CASCADE)
  post = fields.ForeignKeyField("authors_database.Post", related_name="comments", to_field="id", on_delete=fields.CASCADE)

  class Meta:
    table = "comments"