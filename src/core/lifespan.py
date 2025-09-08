from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

from src.core.config import TORTOISE_ORM

async def init_db():
    """
    Инициализирует базу данных с использованием конфигурации Tortoise ORM.
    Если используется aerich для миграций, генерацию схем можно отключить.
    """
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()
    except DBConnectionError as _ex:
        print("Database init error", _ex)


async def close_db() -> None:
    """
    Закрывает все подключения к базе данных.
    """
    await Tortoise.close_connections()


async def lifecycle(app: FastAPI):
    await init_db()
    yield
    await close_db()