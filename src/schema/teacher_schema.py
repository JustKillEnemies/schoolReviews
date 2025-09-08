from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from datetime import date
from src.core.enums import SubjectEnum



class TeacherBaseSchema(BaseModel):
    last_name: str = Field(...,max_length=255)  # Фамилия
    first_name: str = Field(...,max_length=255)# Имя
    middle_name: str = Field(...,max_length=255)# Отчество
    birth_date: date = Field(...)
    hire_date: Optional[date] = Field(None)
    email: str = Field(...,  max_length=255)
    phone: str = Field(...,  max_length=30)
    subject: SubjectEnum

    @field_validator("last_name", "first_name", "middle_name")
    @classmethod
    def capitalize_names(cls, value: str) -> str:
        return value.capitalize() if value else value

    
    @field_validator("subject", mode="before")
    @classmethod
    def capitalize_subject(cls, value):
        # value может быть строкой, надо привести к строке и капитализировать
        if isinstance(value, str):
            value = value.lower().capitalize()
        return value

class TeacherCreateSchema(TeacherBaseSchema):
    pass




class TeacherUpdateSchema(TeacherBaseSchema):
    last_name: Optional[str] = Field(None, max_length=255)
    first_name: Optional[str] = Field(None, max_length=255)
    middle_name: Optional[str] = Field(None, max_length=255)
    birth_date: Optional[date] = Field(None, max_length=255)
    email: Optional[str] = Field(None, max_length=255)
    phone: Optional[str] = Field(None, max_length=255)
    subject: Optional[SubjectEnum] = None

class TeacherOutSchema(TeacherBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)
