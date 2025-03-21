import os

from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

load_dotenv(dotenv_path='.env')

# Описание настройки подключения. Сразу 2 БД подключаем
TORTOISE_ORM = {
    "connections": {
        "authors_database": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("DB_HOST_1"),
                "port": os.getenv("DB_PORT_1"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
                "database": os.getenv("DB_NAME_1"),
            },
        },
        "logs_database": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("DB_HOST_2"),
                "port": os.getenv("DB_PORT_2"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
                "database": os.getenv("DB_NAME_2"),
            },
        },
    },
    "apps": {
        "authors_database": {
            "models": ["app.src.db.authors_database.models"],
            "default_connection": "authors_database",
        },
        "logs_database": {
            "models": ["app.src.db.logs_database.models"],
            "default_connection": "logs_database",
        }
    },
}


async def init_db_tortoise(_app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    # Для автоматической генерации описанных схем
    # await Tortoise.generate_schemas()
    register_tortoise(
        app=_app,
        config=TORTOISE_ORM,
    )
