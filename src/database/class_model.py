from src.core.abstract import BaseORM
from datetime import date
from tortoise import Model, fields
from tortoise.fields import Field


class ClassORM(BaseORM):
    name = fields.CharField(unique=True, max_length=255)


    class Meta:
        table = "classes"
        table_description = "Информация про школьные классы"

    
    def __str__(self):
        return f"Класс: {self.name}"