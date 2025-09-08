from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr
from src.core.abstract import BaseORM
from tortoise import Model, fields
from tortoise.fields import Field

class UserORM(BaseORM):
    username = fields.CharField(min_length=3, max_length=30, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(min_length=8, max_length=255)
    is_active = fields.BooleanField(default=True)

    class Meta:
            table = "users"
            table_description = "Информация про пользователей"
