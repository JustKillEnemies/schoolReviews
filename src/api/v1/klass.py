from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from src.service.klass_service import KlassService
from src.schema.class_schema import (
    ClassCreateSchema,
    ClassOutSchema,
    ClassUpdateSchema
)

router = APIRouter()

@router.post("/create", response_model=ClassOutSchema, description="Добавление класса")
async def create_klass_controller(
    data: ClassCreateSchema
):
    return await KlassService.create_service(data)

@router.get(
    "/get",
    response_model=List[ClassOutSchema],
    description="Получение всех классов"
)
async def get_all_klass_controller():
    return await KlassService.get_all_service()

@router.get("/get/{klass_id}", description="Получение класса по ID")
async def get_klass_controller(
    klass_id: int
):
    return await KlassService.get_service(klass_id)

@router.put("/update/{klass_id}", response_model=ClassOutSchema, description="Обновление класса по ID")
async def update_klass_controller(klass_id: int,
                                  data: ClassUpdateSchema):
    return await KlassService.update_service(klass_id, data)

@router.delete("/delete/{klass_id}", description="Удаление класса по ID")
async def delete_klass_controller(klass_id: int):
    return await KlassService.delete_service(klass_id)