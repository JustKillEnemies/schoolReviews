from src.core.abstract import BaseORM
from datetime import date
from tortoise import Model, fields
from tortoise.fields import Field


class StudentORM(BaseORM):
    last_name = fields.CharField(max_length=255)  # Фамилия
    first_name = fields.CharField(max_length=255)# Имя
    middle_name = fields.CharField(max_length=255)# Отчество
    birth_date = fields.DateField()
    email = fields.CharField(unique=True, max_length=255)
    phone = fields.CharField(unique=True, max_length=30)
    klass = fields.ForeignKeyField('models.ClassORM',
                                       on_delete=fields.CASCADE,
                                       related_name="students",
                                       null=False
                                       )

    class Meta:
        table = "students"
        table_description = "Информация про учеников, учащихся в школе"

    
    def __str__(self):
        return f"Имя - {self.first_name}, фамилия - {self.last_name}, отчество - {self.middle_name}, телефон - {self.phone}"