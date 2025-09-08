from typing import Literal
from pydantic import BaseModel
from pathlib import Path

MODE: Literal["DEV", "PROD"] = "DEV"


if MODE == "DEV":
    APPURL = "127.0.0.1"  # IP данного сервера
    APPPORT = 8000  # Порт данного сервера
else:
    APPURL = "127.0.0.1"  # IP данного сервера
    APPPORT = 8000  # Порт данного сервера

# ======= DataBase Settings ======= #
if MODE == "DEV":
    DATABASE_URL = "sqlite://database.db"
else:
    DATABASE_URL = "postgres://postgres:postgres@localhost:5432/schoolreview"

DATABASE_MODULES = {
    "models": [
        "src.database.teacher_model",
        "src.database.class_model",
        "src.database.student_model",
        "src.database.review_model",
        "src.database.user_model",
        "aerich.models"
    ]
}


TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL,
    },
    "apps":{
        "models": {
            "models": DATABASE_MODULES["models"],
            "default_connection": "default",
        }
    }
}

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    
auth_jwt: AuthJWT = AuthJWT()