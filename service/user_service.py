import datetime
import uuid
from http import HTTPStatus
from typing import Optional

import bcrypt
from flask import abort, Response

from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.user.user_document import UserDocument
from model.repositories.user.user_repository import UserRepository
from model.request.user_login_request import UserLoginRequest
from model.request.user_register_request import UserRegisterRequest
from model.session.user_session import UserSession
from service.session_service import SessionService


class UserService(metaclass=SingletonMeta):
    user_repository = UserRepository()
    session_service = SessionService()

    def find_by_email(self, email: str):
        user = self.user_repository.find_one({"email": email})
        if not user:
            return None

        return UserDocument(user)

    def delete(self, id) -> Optional[UserDocument]:
        deleted_item = self.user_repository.find_by_id(id)
        self.user_repository.delete(id)
        self.session_service.remove_user()
        return deleted_item

    def register(self, request: UserRegisterRequest):
        __validate_register_request__(request)

        hashed = bcrypt.hashpw(request.password2.encode('utf-8'), bcrypt.gensalt())
        document = UserDocument({"name": request.username, "email": request.email, "password": hashed})

        now = datetime.datetime.now()
        if document.id is None or self.user_repository.find_by_id(document.id) is None:
            document = document.copy_with(_id=str(uuid.uuid4()), createdAt=now, updatedAt=now)
        else:
            document = document.copy_with(updatedAt=now)
        self.user_repository.save(document)
        return document

    def login(self, request: UserLoginRequest):
        user = self.find_by_email(request.email)
        __validate_login_request__(request, user)

        self.session_service.set_user(UserSession(user))
        return user

    def logout(self):
        self.session_service.remove_user()


def __validate_register_request__(request: UserRegisterRequest):
    if request.password1 != request.password2:
        abort(Response("passwords do not match", status=HTTPStatus.BAD_REQUEST))


def __validate_login_request__(request: UserLoginRequest, user: UserDocument):
    if user is None:
        abort(Response("User not found", status=HTTPStatus.NOT_FOUND))
    if not bcrypt.checkpw(request.password.encode('utf-8'), user.password):
        abort(Response("Invalid password", status=HTTPStatus.BAD_REQUEST))
