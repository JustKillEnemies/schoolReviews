from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from src.service.student_service import StudentService
from src.database.student_model import StudentORM
from src.schema.student_schema import (
    StudentCreateSchema,
    StudentUpdateSchema,
    StudentOutSchema
)

router = APIRouter()

@router.post("/create",
             response_model=StudentOutSchema,
             description="Создание ученика")
async def create_student_controller(data: StudentCreateSchema):
    return await StudentService.create_service(data)

@router.get("/get", 
            response_model=List[StudentOutSchema], 
            description="Получение всех учеников")
async def get_all_student_controller():
    return await StudentService.get_all_service()

@router.get("/get/{student_id}", 
            response_model=StudentOutSchema, 
            description="Получение ученика по ID")
async def get_student_controller(student_id: int):
    return await StudentService.get_service(student_id)

@router.post("/update/{student_id}",
              response_model=StudentUpdateSchema, 
              description="Обновление данных ученика по ID")
async def update_student_controller(student_id: int, data: StudentUpdateSchema):
    return await StudentService.update_service(student_id, data)

@router.delete("/delete/{student_id}", description="Удаление ученика по ID")
async def delete_student_controller(student_id: int):
    return await StudentService.delete_service(student_id)

