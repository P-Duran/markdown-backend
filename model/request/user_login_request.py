from model.request.default_request import DefaultRequest


class UserLoginRequest(DefaultRequest):
    email = None
    password = None