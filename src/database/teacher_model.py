from src.core.abstract import BaseORM
from datetime import date
from tortoise import Model, fields
from tortoise.fields import Field
from src.core.enums import SubjectEnum
# from enum import Enum

# class SubjectEnum(str, Enum):
#     MATH = "Математика"
#     RUSSIAN = "Русский язык"
#     LITERATURE = "Литература"
#     FOREIGN_LANG = "Иностранный язык"
#     HISTORY = "История"
#     SOCIAL_SCIENCE = "Обществознание"
#     GEOGRAPHY = "География"
#     BIOLOGY = "Биология"
#     PHYSICS = "Физика"
#     CHEMISTRY = "Химия"
#     COMPUTER_SCIENCE = "Информатика"
#     PE = "Физическая культура"
#     TECHNOLOGY = "Технология"
#     SAFETY = "Обж"
#     MUSIC = "Музыка"
#     ART = "Изо"
#     ASTRONOMY = "Астрономия"

class TeacherORM(BaseORM):
    last_name = fields.CharField(max_length=255)  # Фамилия
    first_name = fields.CharField(max_length=255)# Имя
    middle_name = fields.CharField(max_length=255)# Отчество
    birth_date = fields.DateField()
    hire_date = fields.DateField(null=True)
    email = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=30)
    subject = fields.CharEnumField(SubjectEnum, null=True)

    # subjects = fields.ManyToManyField('models.SubjectORM',
    #                                     related_name="teachers",
    #                                     )

    class Meta:
        table = "teachers"
        table_description = "Информация про учителей, работающих в школе"
        # unique_together = ("email", "subject", "phone")
        unique_together = (
            ("email", "phone", "subject"), 
        )
    
    def __str__(self):
        return f"Имя - {self.first_name}, фамилия - {self.last_name}, отчество - {self.middle_name}, телефон - {self.phone}"