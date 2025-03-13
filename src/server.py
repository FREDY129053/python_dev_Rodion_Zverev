from fastapi import FastAPI
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from src.db import init_db_tortoise
from src.router import router_comments, router_general


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
  await init_db_tortoise(_app)
  yield

def create_app() -> FastAPI:
  _app = FastAPI(
    title="Simple Info API",
    docs_url="/docs",
    lifespan=lifespan,
  )

  _app.include_router(router_comments)
  _app.include_router(router_general)
  

  return _app

app = create_app()