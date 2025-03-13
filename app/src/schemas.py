import datetime
from pydantic import BaseModel, field_validator

# Схема для возврата значения из эндпоинта /comments
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


# Модель для создания комментария
class CreateCommentModel(BaseModel):
  text: str
  author: str
  post: int


# Модель для создания записи в логах
class CreateLogModel(BaseModel):
  datetime: datetime.datetime
  user_id: int
  event_type: int