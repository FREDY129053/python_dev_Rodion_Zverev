from app.src.db.authors_database.models import Comment, User, Post

from tortoise.functions import Count
from typing import List

async def getUserCommentsInfo(login: str) -> List[Comment] | None:
  """Получение информации о комментариях пользователя"""
  if not await _isUserExist(login=login):  # Если пользователя нет, то будем поднимать ошибку
    return None
  
  # Сырой SQL запрос
  # select
  #   t2.login as commenter_login,
  #   t3.header as post_header,
  #   t4.login as post_author_login,
  #   count(t1.id) as comment_count
  # from comments as t1
  # join users t2 on t2.id = t1.author_id
  # join posts t3 on t1.post_id = t3.id
  # join users t4 on t3.author_id = t4.id
  # where t2.login = 'login_1' -- login_1 это пример
  # group by t2.login, t3.header, t4.login;

  result = (
        await Comment
        .filter(author__login=login)
        .annotate(comment_count=Count("id"))
        .select_related("author", "post__author") 
        .group_by("author__login", "post__header", "post__author__login") 
        .values(
            commenter_login="author__login",
            post_header="post__header",
            post_author_login="post__author__login", 
            comments_count="comment_count",
        )
    )
  
  return result


async def insertComment(text: str, author: str, post: int) -> Comment:
  """Запись комментария в таблицу"""
  author = await User.get(login=author)
  post = await Post.get(id=post)
  
  return await Comment.create(text=text, author=author, post=post)

async def _isUserExist(login: str) -> bool:
  """Проверка на существование пользователя"""
  user = await User.get_or_none(login=login)
  if user:
    return True
  
  return False