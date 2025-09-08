import jwt
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tortoise.exceptions import IntegrityError
from passlib.context import CryptContext

from src.core.config import auth_jwt

from src.database.user_model import UserORM
from src.schema.user_schema import (
    UserCreateSchema,
    UserLoginSchema,
    UserOutSchema,
    TokenSchema,
)
from src.utils.exceptions import UserNotFoundException, UserAlreadyExistsException, WrongPasswordException, InvalidTokenException, WrongTokenException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
PRIVATE_KEY = auth_jwt.private_key_path.read_text()
PUBLIC_KEY = auth_jwt.public_key_path.read_text()
ACCESS_TOKEN_EXPIRE_MINUTES = 0.5
REFRESH_TOKEN_EXPIRE_DAYS = 7
ALGORITHM = auth_jwt.algorithm



def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=0.5))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)



class UserService:
    @staticmethod
    async def create_user_service(data: UserCreateSchema) -> UserOutSchema:
        hashed_password = get_password_hash(data.password)
        try:
            obj = await UserORM.create(
                username=data.username,
                email=data.email,
                password=hashed_password
            )
            return UserOutSchema.model_validate(obj)
        except IntegrityError:
            raise UserAlreadyExistsException()
        
    @staticmethod
    async def login_user_service(data: UserLoginSchema) -> dict:

        user = await UserORM.get_or_none(username=data.username)
        if not user:
            raise UserNotFoundException()
        
        if not verify_password(data.password, user.password):
            raise WrongPasswordException()
        
        token_data = {"sub": str(user.id)}
        access_token = create_access_token(token_data)
        refresh_token = create_refresh_token(token_data)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user_id": user.id
        }
    
    @staticmethod
    async def refresh_access_token_service(refresh_token: str) -> TokenSchema:
        try:
            payload = jwt.decode(refresh_token, PUBLIC_KEY, algorithms=[ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise InvalidTokenException()
        except jwt.InvalidTokenError:
            raise WrongTokenException()
        
        if payload.get("type") != "refresh": raise Exception("Это не refresh-токен")

        user_id = payload.get("sub")
        return TokenSchema(
            access_token=create_access_token({"sub": user_id}),
            refresh_token=refresh_token,  
            token_type="bearer",
            user_id=int(user_id)
        )


    @staticmethod
    async def get_current_user(user_id: int) -> UserOutSchema:
        user = await UserORM.get_or_none(id=user_id)
        if not user:
            raise UserNotFoundException()
        return UserOutSchema.model_validate(user)

    @staticmethod
    async def logout_user_service() -> dict:
        """
        Stateless logout — просто подсказка клиенту удалить токены
        """
        return {
            "message": "Вы успешно вышли из системы. Пожалуйста удалите токены на стороне пользователя"
        }