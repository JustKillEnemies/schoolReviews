from src.database.review_model import ReviewORM
from src.database.teacher_model import TeacherORM
from src.database.student_model import StudentORM
from src.schema.review_schema import ReviewBaseSchema, ReviewOutSchema, ReviewCreateSchema
from src.schema.enum import ReviewCriteria
from typing import Optional, List
from tortoise.expressions import Q
from src.utils.exceptions import ReviewNotFoundException, TeacherNotFoundException, StudentNotFoundException

class ReviewService:
    @staticmethod
    async def create_service(data: ReviewCreateSchema):

        if not await TeacherORM.exists(id=data.teacher_id):
            raise TeacherNotFoundException()
        
        if not await StudentORM.exists(id=data.student_id):
            raise StudentNotFoundException()

        obj = await ReviewORM.create(**data.model_dump())
        return ReviewOutSchema.model_validate(obj)
    
    @staticmethod
    async def get_all_service():
        reviews =  await ReviewORM.all().prefetch_related("student", "teacher")

        return [ReviewOutSchema.model_validate(review) for review in reviews]
    
    @staticmethod
    async def get_all_certain_service(current_teacher_id: int):
        reviews =  await ReviewORM.all().prefetch_related("student", "teacher").filter(teacher_id=current_teacher_id)
        
        return [ReviewOutSchema.model_validate(review) for review in reviews]
    
    @staticmethod
    async def delete_service(revied_id: int):
        review = await ReviewORM.get_or_none(id=revied_id)
        if not review:
            raise ReviewNotFoundException()
        
        await review.delete()
        return {
            "id": revied_id,
            "detail": "success"
        }

    