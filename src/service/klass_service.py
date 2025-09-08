from typing import Optional, List
from src.database.class_model import ClassORM
from src.schema.class_schema import(ClassCreateSchema,
                                    ClassUpdateSchema,
                                    ClassOutSchema
                                    )
from src.utils.exceptions import KlassNotFoundException


class KlassService:

    @staticmethod
    async def create_service(data: ClassCreateSchema):
        obj = await ClassORM.create(**data.dict())
        return ClassOutSchema.model_validate(obj)
    
    @staticmethod
    async def get_all_service():
        objects = await ClassORM.all()
        return [ClassOutSchema.model_validate(obj) for obj in objects]
    
    @staticmethod
    async def get_service(klass_id: int):
        obj = await ClassORM.get_or_none(id=klass_id)
        if obj is None:
            raise KlassNotFoundException()
        return ClassOutSchema.model_validate(obj)
    
    @staticmethod
    async def update_service(klass_id: int, data: ClassUpdateSchema):
        obj = await ClassORM.get_or_none(id=klass_id)
        if obj is None:
            raise KlassNotFoundException()
        await obj.update_from_dict(data.dict(exclude_unset=True)).save()
        return ClassOutSchema.model_validate(obj)
    
    @staticmethod
    async def delete_service(klass_id: int):
        obj = await ClassORM.get_or_none(id=klass_id)
        if obj is None:
            raise KlassNotFoundException()
        await obj.delete()
        return {
            "klass_id": klass_id,
            "detail": "success"
        }

