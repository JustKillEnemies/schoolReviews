from enum import Enum, IntEnum


class SubjectEnum(str, Enum):
    MATH = "Математика"
    RUSSIAN = "Русский язык"
    LITERATURE = "Литература"
    FOREIGN_LANG = "Иностранный язык"
    HISTORY = "История"
    SOCIAL_SCIENCE = "Обществознание"
    GEOGRAPHY = "География"
    BIOLOGY = "Биология"
    PHYSICS = "Физика"
    CHEMISTRY = "Химия"
    COMPUTER_SCIENCE = "Информатика"
    PE = "Физическая культура"
    TECHNOLOGY = "Технология"
    SAFETY = "Обж"
    MUSIC = "Музыка"
    ART = "Изо"
    ASTRONOMY = "Астрономия"


class ReviewCriteria(IntEnum):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5