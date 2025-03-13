from typing import Union, List
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse

from src.schemas import CommentsModel, ErrorModel, GeneralModel
from src.repository.comments import getUserCommentsInfo
from src.repository.logs import getGeneralInfo


router_comments = APIRouter(prefix='/api', tags=["Comments"])
router_general = APIRouter(prefix='/api', tags=["General"])

@router_comments.get('/comments', response_model=Union[List[CommentsModel], ErrorModel], responses={404: {"model": ErrorModel}})
async def get_comment_info(user_login: str):
  """### Вывод данных о коментариях пользователя"""
  result = await getUserCommentsInfo(login=user_login)

  if result is None:
    return JSONResponse(content={"error": "user not found"}, status_code=404)
  
  return result

@router_general.get('/general', response_model=Union[List[GeneralModel], ErrorModel], responses={404: {"model": ErrorModel}})
async def get_general_info(user_login: str):
  """### Вывод статистики пользователя за **сутки**"""
  result = await getGeneralInfo(login=user_login)

  if result is None:
    return JSONResponse(content={"error": "user not found"}, status_code=404)
  
  return result