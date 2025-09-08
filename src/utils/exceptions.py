from fastapi import status
from src.core.abstract import BaseHTTPException


def generate_responses(errors: list[BaseHTTPException]):
    data = {}
    for i in errors:
        data[i.status_code] = {"description": i.detail}
    return data

class KlassNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого класса не существует"


class KlassAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой класс уже существует"

class SubjectNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого предмета не существует"


class SubjectAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой предмет уже существует"

class StudentNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого ученика не существует"


class StudentAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой ученик уже существует"

class TeacherNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого преподавателя не существует"


class TeacherAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой преподаватель уже существует"

class ReviewNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого отзыва не существует"


class PasswordLengthException(BaseHTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Пароль должен быть от 8 до 255 символов"

class UserAlreadyExistsException(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой пользователь уже существует"

class UserNotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого пользователя не существует"


class WrongCredentialsException(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неправильный логин или пароль"

class WrongPasswordException(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Неправильный пароль"

class InvalidTokenException(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истёк"

class WrongTokenException(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный токен"