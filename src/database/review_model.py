from src.core.abstract import BaseORM
from datetime import date
from tortoise import Model, fields
from tortoise.fields import Field
from src.core.enums import ReviewCriteria



class ReviewORM(BaseORM):
    review_text = fields.TextField(description="Текст отзыва")
    teaching_skill = fields.IntEnumField(ReviewCriteria, description="Умение преподавать")
    communication = fields.IntEnumField(ReviewCriteria, description="Умение общаться с учениками")
    fairness = fields.IntEnumField(ReviewCriteria, description="Справедливость оценивания")

    student = fields.ForeignKeyField("models.StudentORM",
                                        null=True,
                                        on_delete=fields.CASCADE,
                                        related_name="reviews"
                                        )
    
    teacher = fields.ForeignKeyField("models.TeacherORM",
                                        null=True,
                                        on_delete=fields.CASCADE,
                                        related_name="reviews")

    class Meta:
        table = "reviews"
        table_description = "Информация про отзывы учеников о преподавателях"
        unique_together = (("student", "teacher"),)
    
    # def __str__(self):
    #     return f"Отзыв: {self.review_text}"