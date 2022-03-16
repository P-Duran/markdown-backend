from flask import Blueprint, request

from model.decorators.controller_decorators import requires_login, requires_roles
from model.enum.role import Role
from model.request.user_login_request import UserLoginRequest
from model.request.user_register_request import UserRegisterRequest
from service.user_service import UserService

user_service = UserService()

user_controller = Blueprint('authentication', __name__, url_prefix='/authentication')


@user_controller.route('/register', methods=["POST"])
def register_user():
    user_request = UserRegisterRequest(request.form.to_dict())
    user = user_service.register(user_request)
    return "User '" + user.name + "' correctly registered"


@user_controller.route("/login", methods=["POST"])
def login():
    login_request = UserLoginRequest(request.form.to_dict())
    user = user_service.login(login_request)
    return "User '" + user.name + "' correctly logged"


@requires_login
@user_controller.route("/logout", methods=["POST"])
def logout():
    user_service.logout()


@user_controller.route("/test")
@requires_roles([Role.ADMIN])
@requires_login
def test():
    a = None
    a.roi()
    return "test"
