from http import HTTPStatus
from typing import List

from flask import abort, Response
from functools import wraps
from model.enum.role import Role
from service.session_service import SessionService
from service.user_service import UserService

session_service = SessionService()
user_service = UserService()

def requires_login(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if session_service.current_user() is None:
            return abort(Response("User needs to be authenticated"), HTTPStatus.UNAUTHORIZED)
        return f(*args, **kwargs)
    return wrapped

def requires_roles(roles: List[Role]):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            current_user = session_service.current_user()
            if not current_user:
                return abort(Response("User needs to be authenticated"), HTTPStatus.FORBIDDEN)
            user = user_service.find_by_username(current_user)

            if user is None or Role[user.role] not in roles:
                return abort(Response("Current user does not have the required roles"), HTTPStatus.FORBIDDEN)
            return f(*args, **kwargs)
        return wrapped
    return decorator