from pydantic import BaseModel, Field, ConfigDict
from typing import  Optional


class ClassBaseSchema(BaseModel):
    name: str = Field(..., max_length=3)


class ClassCreateSchema(ClassBaseSchema):
    pass

class ClassUpdateSchema(ClassBaseSchema):
    name: Optional[str] = Field(None, max_length=3)


class ClassOutSchema(ClassBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)
