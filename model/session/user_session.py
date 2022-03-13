from model.enum.role import Role
from model.request.default_request import DefaultRequest


class UserSession(DefaultRequest):
    _id = None
    name = None
    email = None
    role: Role = None