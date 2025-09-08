from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from datetime import date

class StudentBaseSchema(BaseModel):
    last_name: str = Field(...,max_length=255)  # Фамилия
    first_name: str = Field(...,max_length=255)# Имя
    middle_name: str = Field(...,max_length=255)# Отчество
    birth_date: date = Field(...)
    email: str = Field(...,  max_length=255)
    phone: str = Field(...,  max_length=30)
    klass_id: int

    @field_validator("last_name", "first_name", "middle_name")
    @classmethod
    def capitalize_names(cls, value: str) -> str:
        return value.capitalize() if value else value
    

class StudentCreateSchema(StudentBaseSchema):
    pass




class StudentUpdateSchema(StudentBaseSchema):
    last_name: Optional[str] = Field(None, max_length=255)
    first_name: Optional[str] = Field(None, max_length=255)
    middle_name: Optional[str] = Field(None, max_length=255)
    birth_date: Optional[date] = Field(None)
    email: Optional[str] = Field(None, max_length=255)
    phone: Optional[str] = Field(None, max_length=255)
    klass_id: Optional[int] = Field(None)


class StudentOutSchema(StudentBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)
