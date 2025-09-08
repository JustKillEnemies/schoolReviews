from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import  Optional
from src.schema.enum import ReviewCriteria

class ReviewBaseSchema(BaseModel):
    review_text: str = Field()
    teaching_skill: ReviewCriteria
    communication: ReviewCriteria
    fairness: ReviewCriteria

    student_id: Optional[int] = Field(None, description="ID студента, оставившего отзыв")
    teacher_id: int = Field(description="ID преподавателя, к которому относится отзыв")

class ReviewCreateSchema(ReviewBaseSchema):
    pass

    @field_validator("review_text")
    @classmethod
    def capitalize_names(cls, value: str) -> str:
        return value.capitalize() if value else value

class ReviewUpdateSchema(ReviewBaseSchema):
    review_text: Optional[str] = Field()
    teaching_skill: Optional[int] 
    communication: Optional[int] 
    fairness: Optional[int] 


class ReviewOutSchema(ReviewBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)