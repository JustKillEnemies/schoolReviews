from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from src.service.review_service import ReviewService
from src.database.review_model import ReviewORM
from src.schema.review_schema import (
    ReviewCreateSchema,
    ReviewUpdateSchema,
    ReviewOutSchema
)
from src.schema.enum import ReviewCriteria

router = APIRouter()

@router.post("/create", response_model=ReviewOutSchema, description="Создание отзыва")
async def create_review_controller(data: ReviewCreateSchema):
    return await ReviewService.create_service(data)

@router.get("/get", response_model=List[ReviewOutSchema], description="Получение всех отзывов")
async def get_all_review_controller():
    return await ReviewService.get_all_service()

@router.get("/get/all/{current_teacher_id}", response_model=List[ReviewOutSchema], description="Получение всех отзывов на конкретного преподавателя по ID")
async def get_all_review_on_teacher_controller(current_teacher_id: int):
    return await ReviewService.get_all_certain_service(current_teacher_id)

@router.get("/delete/{review_id}", description="Удаление отзыва")
async def delete_controller(review_id: int):
    return await ReviewService.delete_service(review_id)