from typing import Any
from fastapi import HTTPException
import datetime
from tortoise import Model, fields
from tortoise.signals import pre_save
from tortoise.fields import Field

async def pre_save_model(
    sender: Any,
    instance: "BaseORM",
    using_db: str,
    update_fields: list[str],
) -> None:
    instance.version += 1


class BaseORM(Model):
    id = fields.IntField(pk=True)
    created_at: datetime = fields.DatetimeField(auto_now_add=True) # type: ignore
    updated_at: datetime = fields.DatetimeField(auto_now=True) # type: ignore
    is_deleted = fields.BooleanField(default=False) # Для возможности не удалять объекты из бд, но помечать их как удаленные
    version = fields.IntField(default=0) # Для возможности отследить кол-во изменений объекта

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        pre_save(cls)(pre_save_model)

    class Meta:
        abstract=True


class BaseHTTPException(HTTPException):
    status_code = 200
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

    @classmethod
    def get_dict(cls):
        return {"detail": cls.detail}