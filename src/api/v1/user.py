from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordBearer
import jwt
from typing import Annotated

from src.service.user_service import UserService
from src.schema.user_schema import (
    UserCreateSchema,
    UserLoginSchema,
    UserOutSchema,
    TokenSchema,
)

from src.utils.exceptions import InvalidTokenException, WrongTokenException

from src.core.config import auth_jwt


router = APIRouter()
PUBLIC_KEY = auth_jwt.public_key_path.read_text()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login")

def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> int:
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=auth_jwt.algorithm)
        return int(payload.get("sub"))
    except jwt.ExpiredSignatureError:
        raise InvalidTokenException()
    except jwt.InvalidTokenError:
        raise WrongTokenException()
    

@router.post("/register",
             response_model=UserOutSchema,
             description="Регистрация пользователя"
             )
async def register_user(data: UserCreateSchema):
    return await UserService.create_user_service(data)


@router.post("/login",
             response_model=TokenSchema,
             description="Вход в систему")
async def login_user(data: UserLoginSchema):
    return await UserService.login_user_service(data)


@router.get("/me", response_model=UserOutSchema)
async def get_me(user_id: Annotated[int, Depends(get_current_user_id)]):
    return await UserService.get_current_user(user_id)

@router.post("/refresh", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    return await UserService.refresh_access_token_service(refresh_token)

@router.post("/logout")
async def logout_user():
    return await UserService.logout_user_service()