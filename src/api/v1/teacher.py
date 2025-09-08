from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from src.schema.teacher_schema import TeacherOutSchema, TeacherCreateSchema, TeacherUpdateSchema
from src.database.teacher_model import TeacherORM
from src.service.teacher_service import TeacherService
from src.core.enums import SubjectEnum

router = APIRouter()

@router.post(
        "/create",
        response_model=TeacherOutSchema, 
        description="Создание преподавателя"
)
async def create_teacher_controller(data: TeacherCreateSchema):
    return await TeacherService.create_service(data)

@router.get("/get",
            response_model=List[TeacherOutSchema],
            description="Получение всех преподавателей с фильтрацией")
async def get_all_teachers_controller(subject: Optional[List[SubjectEnum]] = Query(None, description="Филтрация по предметам")):
    return await TeacherService.get_all_service(subject=subject)


@router.get("/get/{teacher_id}",
            response_model=TeacherOutSchema,
            description="Получение преподавателя по ID")
async def get_teacher_controller(teacher_id: int):
    return await TeacherService.get_service(teacher_id)

@router.get("/search",
            response_model=List[TeacherOutSchema],
            description="Получение преподавателя по фамилии")
async def get_teacher_surname_controller(last_name: str):
    return await TeacherService.get_by_surname_service(last_name)

@router.delete("/delete/{teacher_id}",
               description="Удаление преподавателя по ID")
async def delete_teacher_controller(teacher_id: int):
    return await TeacherService.delete_service(teacher_id)

@router.post("/update/{teacher_id}", response_model=TeacherOutSchema, description="Изменение данных преподавателя по ID")
async def update_teacher_controller(teacher_id: int, data: TeacherUpdateSchema):
    return await TeacherService.update_service(teacher_id, data)