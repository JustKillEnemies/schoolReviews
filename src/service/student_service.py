from src.database.student_model import StudentORM
from src.schema.student_schema import (
    StudentCreateSchema, 
    StudentOutSchema, 
    StudentUpdateSchema
    )
from src.utils.exceptions import StudentNotFoundException, KlassNotFoundException
from tortoise import fields
from src.database.class_model import ClassORM
class StudentService:
    
    @staticmethod
    async def create_service(data: StudentCreateSchema):
        if await ClassORM.exists(id=data.klass_id):
            obj = await StudentORM.create(**data.model_dump())
        else:
            raise KlassNotFoundException()
        return StudentOutSchema.model_validate(obj)
    
    @staticmethod
    async def get_all_service():
        students = await StudentORM.all()
        return [StudentOutSchema.model_validate(obj) for obj in students]
    
    @staticmethod
    async def get_service(student_id: int):
        obj = await StudentORM.get_or_none(id=student_id)
        if obj is None:
            raise StudentNotFoundException()
        return StudentOutSchema.model_validate(obj)
    
    @staticmethod
    async def update_service(student_id: int, data: StudentUpdateSchema):
        obj = await StudentORM.get_or_none(id=student_id)
        if obj is None:
            raise StudentNotFoundException()
        
        await obj.update_from_dict(data.model_dump(exclude_unset=True)).save()

        return StudentOutSchema.model_validate(obj)

    @staticmethod
    async def delete_service(student_id: int):     
        obj = await StudentORM.get_or_none(id=student_id)
        if obj is None:
            raise StudentNotFoundException()
        await obj.delete()
        return {"student_id": student_id,
                "detail": "success"}
