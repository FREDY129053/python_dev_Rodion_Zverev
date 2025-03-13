import datetime
from typing import List

from app.src.db.logs_database.models import Log, SpaceType, EventType
from app.src.db.authors_database.models import User

from enum import IntEnum
from tortoise.expressions import Q, RawSQL
from tortoise.functions import Count

# Чуть лень стало вводить event_type в тело запроса)
class SpaceTypeEnum(IntEnum):
  GLOBAL = 1
  BLOG = 2
  POST = 3


async def getGeneralInfo(login: str | None, id: int | None) -> List[Log]:
  """Получение информации о дейтсвиях пользователя"""
  
  user_id = None

  # Если передается 2 значения, то поиск будет производиться по логину и в случае провала по id
  # Если передается логин, ищем по нему
  if login is not None:
    user_id = await _getUserIDByLogin(login=login)
    # Если в 1ой БД не нашли по логину, то даем шанс найти по id в самой таблице логов
    if user_id is None:
      user_id = id
  elif id is not None:
    user_id = id
  
  # Сырой SQL запрос
  # select 
  #   date(datetime) as date, 
  #   count(case when event_type_id = 1 then 1 end) as login_count, 
  #   count(case when event_type_id = 5 then 1 end) as logout_count, 
  #   count(*) filter (where event_type_id = 3 or event_type_id = 4) blog_events_count
  # from logs
  # where user_id = 1  -- 1 это для примера
  # group by date;

  result = await Log \
    .annotate(
      date=RawSQL("DATE(datetime)"),
      login_count=Count("id", _filter=Q(event_type_id=1)),
      logout_count=Count("id", _filter=Q(event_type_id=5)),
      blog_events_count=Count("id", _filter=Q(event_type_id=3) | Q(event_type_id=4)),
    ) \
    .filter(user_id=user_id) \
    .group_by("date") \
    .order_by("date") \
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
  

async def insertLog(datetime: datetime.datetime, user_id: int, event_type: int) -> Log:
  """Запись лога в таблицу"""
  event_type = await EventType.get(id=event_type)
  space_type_enum = None
  match event_type.id:
    case 1 | 5:
      space_type_enum = SpaceTypeEnum.GLOBAL
    case 3 | 4:
      space_type_enum = SpaceTypeEnum.BLOG
    case 2:
      space_type_enum = SpaceTypeEnum.POST
      
  space_type = await SpaceType.get(id=space_type_enum.value)
  
  return await Log.create(datetime=datetime, user_id=user_id, space_type=space_type, event_type=event_type)