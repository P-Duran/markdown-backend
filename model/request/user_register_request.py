from model.request.default_request import DefaultRequest


class UserRegisterRequest(DefaultRequest):
    username = None
    email = None
    password1 = None
    password2 = None