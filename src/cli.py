from uvicorn import run
from fastapi import FastAPI
from src.core.lifespan import lifecycle
from src.core import config
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import (
    klass, student, teacher, review, user
)
app = FastAPI(
    docs_url="/docs",
    lifespan=lifecycle,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(klass.router, prefix="/api/v1/klass", tags=["klass"])
# app.include_router(student.router, prefix="/api/v1/student", tags=["student"])
# app.include_router(teacher.router, prefix="/api/v1/teacher", tags=["teacher"])
# app.include_router(review.router, prefix="/api/v1/review", tags=["review"])
app.include_router(user.router, prefix="/api/v1/user", tags=["user"])


def main():
    run(app, host=config.APPURL, port=config.APPPORT)

