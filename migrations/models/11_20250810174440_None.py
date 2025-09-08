from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "teachers" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0,
    "version" INT NOT NULL DEFAULT 0,
    "last_name" VARCHAR(255) NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "middle_name" VARCHAR(255) NOT NULL,
    "birth_date" DATE NOT NULL,
    "hire_date" DATE,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(30) NOT NULL,
    "subject" VARCHAR(19) /* MATH: Математика\nRUSSIAN: Русский язык\nLITERATURE: Литература\nFOREIGN_LANG: Иностранный язык\nHISTORY: История\nSOCIAL_SCIENCE: Обществознание\nGEOGRAPHY: География\nBIOLOGY: Биология\nPHYSICS: Физика\nCHEMISTRY: Химия\nCOMPUTER_SCIENCE: Информатика\nPE: Физическая культура\nTECHNOLOGY: Технология\nSAFETY: Обж\nMUSIC: Музыка\nART: Изо\nASTRONOMY: Астрономия */,
    CONSTRAINT "uid_teachers_email_3888bf" UNIQUE ("email", "phone", "subject")
) /* Информация про учителей, работающих в школе */;
CREATE TABLE IF NOT EXISTS "classes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0,
    "version" INT NOT NULL DEFAULT 0,
    "name" VARCHAR(255) NOT NULL UNIQUE
) /* Информация про школьные классы */;
CREATE TABLE IF NOT EXISTS "students" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0,
    "version" INT NOT NULL DEFAULT 0,
    "last_name" VARCHAR(255) NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "middle_name" VARCHAR(255) NOT NULL,
    "birth_date" DATE NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "phone" VARCHAR(30) NOT NULL UNIQUE,
    "klass_id" INT NOT NULL REFERENCES "classes" ("id") ON DELETE CASCADE
) /* Информация про учеников, учащихся в школе */;
CREATE TABLE IF NOT EXISTS "reviews" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0,
    "version" INT NOT NULL DEFAULT 0,
    "review_text" TEXT NOT NULL /* Текст отзыва */,
    "teaching_skill" SMALLINT NOT NULL /* Умение преподавать */,
    "communication" SMALLINT NOT NULL /* Умение общаться с учениками */,
    "fairness" SMALLINT NOT NULL /* Справедливость оценивания */,
    "student_id" INT REFERENCES "students" ("id") ON DELETE CASCADE,
    "teacher_id" INT REFERENCES "teachers" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_reviews_student_b5730a" UNIQUE ("student_id", "teacher_id")
) /* Информация про отзывы учеников о преподавателях */;
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
