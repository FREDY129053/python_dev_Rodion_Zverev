from src.db.logs_database.models import Log
from src.db.authors_database.models import User

from tortoise.expressions import Q, RawSQL
from tortoise.functions import Count

async def getGeneralInfo(login: str):
  user_id = await _getUserIDByLogin(login=login)
  if user_id is None:
    return None
  
  result = await Log \
    .annotate(
      date=RawSQL("DATE(datetime)"),
      login_count=Count("id", _filter=Q(event_type_id=1)),
      logout_count=Count("id", _filter=Q(event_type_id=5)),
      blog_events_count=Count("id", _filter=Q(event_type_id=3) | Q(event_type_id=4)),
    ) \
    .filter(user_id=user_id) \
    .group_by("date") \
    .values(
      "date", 
      "login_count", 
      "logout_count", 
      "blog_events_count",
    )

  return result


async def _getUserIDByLogin(login: str) -> int | None:
  """Получение ID пользователя по логину"""
  user = await User.get_or_none(login=login)
  if user:
    return user.id
  
  return None
  