from src.database.teacher_model import TeacherORM
from src.schema.teacher_schema import TeacherOutSchema, TeacherCreateSchema, TeacherUpdateSchema
from src.utils.exceptions import TeacherNotFoundException, TeacherAlreadyExistsException, SubjectNotFoundException
from tortoise.expressions import Q
from src.core.enums import SubjectEnum
from typing import Optional, List


class TeacherService:

    @staticmethod
    async def get_all_service(subject: Optional[List[SubjectEnum]] = None):
        query = TeacherORM.all()
        if subject:
            query = query.filter(subject__in=subject)

        teachers = await query

        return [TeacherOutSchema.model_validate(teacher) for teacher in teachers]

    @staticmethod
    async def get_service(teacher_id: int):
        teacher = await TeacherORM.get_or_none(id=teacher_id)
        if not teacher:
            raise TeacherNotFoundException()
        
        return TeacherOutSchema.model_validate(teacher)

    @staticmethod
    async def get_by_surname_service(last_name: str):
        teachers = await TeacherORM.filter(Q(last_name__icontains=last_name))
        return [TeacherOutSchema.model_validate(teacher) for teacher in teachers]
    
    @staticmethod
    async def create_service(data: TeacherCreateSchema):
        # Проверяем, что предмет из enum
        if data.subject not in SubjectEnum:
            raise ValueError(f"Неверный предмет: {data.subject}")

        existing_teacher = await TeacherORM.filter(
            email=data.email,
            phone=data.phone,
            subject=data.subject.value
        ).exists()

        if existing_teacher:
            raise TeacherAlreadyExistsException()
        
        teacher = await TeacherORM.create(
            last_name=data.last_name,
            first_name=data.first_name,
            middle_name=data.middle_name,
            birth_date=data.birth_date,
            hire_date=data.hire_date,
            email=data.email,
            phone=data.phone,
            subject=data.subject.value 
        )

        return TeacherOutSchema.model_validate(teacher)
    
    @staticmethod
    async def delete_service(teacher_id: int):
        teacher = await TeacherORM.get_or_none(id=teacher_id)
        if teacher is None:
            raise TeacherNotFoundException()
        await teacher.delete()
        return {"teacher_id": teacher_id,
                "detail": "success"}
    
    @staticmethod
    async def update_service(teacher_id: int, data: TeacherUpdateSchema):
        obj = await TeacherORM.get_or_none(id=teacher_id)
        if obj is None:
            raise TeacherNotFoundException()
        
        await obj.update_from_dict(data.model_dump(exclude_unset=True)).save()
    

        return TeacherOutSchema.model_validate(obj)