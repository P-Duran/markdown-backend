from http import HTTPStatus
from typing import List

from flask import abort, Response
from functools import wraps
from model.enum.role import Role
from service.user_service import UserService

user_service = UserService()

def requires_login(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if user_service.current_user() is None:
            return abort(Response("User needs to be authenticated"), HTTPStatus.UNAUTHORIZED)
        return f(*args, **kwargs)
    return wrapped

def requires_roles(roles: List[Role]):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user = user_service.current_user()
            if user is None or Role[user.role] not in roles:
                return abort(Response("Current user does not have the required roles"), HTTPStatus.FORBIDDEN)
            return f(*args, **kwargs)
        return wrapped
    return decorator