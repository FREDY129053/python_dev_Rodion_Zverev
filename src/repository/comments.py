from src.db.authors_database.models import Comment

from tortoise.functions import Count
# from tortoise import connections

async def getUserCommentsInfo(login: str):
  # _ = connections.get("authors_database")

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
  
  if len(result) < 1:
    return None
  
  return result