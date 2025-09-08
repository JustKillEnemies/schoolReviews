from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator
from typing import Optional

class UserBaseSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr = Field(..., max_length=255)
    is_active: Optional[bool] = Field(default=True)


class UserCreateSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=255)


class UserLoginSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=8, max_length=255)


class UserOutSchema(UserBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user_id: int