from typing import Dict, List
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from app.src.schemas import CommentsModel, GeneralModel, CreateCommentModel, CreateLogModel
from app.src.repository.comments import getUserCommentsInfo, insertComment
from app.src.repository.logs import getGeneralInfo, insertLog


# Роутеры можно распихать в разные файлы, но они небольшие в целом
router_comments = APIRouter(prefix='/api', tags=["Comments"])
router_general = APIRouter(prefix='/api', tags=["General"])


@router_comments.get(
    '/comments', 
    response_model=List[CommentsModel],
    responses={
      status.HTTP_404_NOT_FOUND: {"description": "User not found"},
    }
)
async def get_comment_info(user_login: str):
  """### Вывод данных о коментариях пользователя"""
  result = await getUserCommentsInfo(login=user_login)

  if result is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
  
  return result


@router_comments.post(
    '/comments',
    response_model=Dict[str, str],
    responses={
      status.HTTP_400_BAD_REQUEST: {"description": "Invalid data"},
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_comment(comment: CreateCommentModel):
  """### Создание комментария в таблице"""
  try:
    await insertComment(
      text=comment.text,
      author=comment.author,
      post=comment.post,
    )
    return JSONResponse(content={"message": "comment create"}, status_code=status.HTTP_201_CREATED)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router_general.get('/general', response_model=List[GeneralModel])
async def get_general_info(user_login: str | None = None, user_id: int | None = None):
  """### Этот эндпоинт предоставляет статистику действий пользователя за **каждый день** из таблицы. \\

     Логика поиска пользователя: \\
     - Если передан только логин, то сначала выполняется определение ID по логину(с помощью таблицы **users** из 1ой БД) и затем поиск информации об этом пользователе. \\
     - Если передан только ID, то поиск происходит напрямую в таблице **logs**.\\
     - Если переданы оба параметра, сначала выполняется поиск ID в первой БД. Если пользователь не найден, то будет предпринята попытка найти его в таблице **logs**.
  """
  result = await getGeneralInfo(login=user_login, id=user_id)
  
  return result


@router_general.post(
    '/general', 
    response_model=Dict[str, str],
    responses={
      status.HTTP_400_BAD_REQUEST: {"description": "Invalid data"},
    },
    status_code=status.HTTP_201_CREATED,
  )
async def create_log(log: CreateLogModel):
  """### Создание записи в таблице логов"""
  try:
    await insertLog(
      datetime=log.datetime,
      user_id=log.user_id,
      event_type=log.event_type,
    )
    return JSONResponse(content={"message": "log create"}, status_code=status.HTTP_201_CREATED)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))