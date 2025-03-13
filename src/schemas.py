import datetime
from pydantic import BaseModel, field_validator

class CommentsModel(BaseModel):
  commenter_login: str
  post_header: str
  post_author_login: str
  comments_count: int

# Для даты можно использовать валидатор для даты, например для преобразования в формат DD-MM-YYYY
class GeneralModel(BaseModel):
  date: datetime.date
  login_count: int
  logout_count: int
  blog_events_count: int

  # @field_validator("date", mode="before")
  # def validate_date(cls, value):
  #   ...

class ErrorModel(BaseModel):
  error: str = "user not found"