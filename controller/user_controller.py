from flask import Blueprint, request, jsonify, session
from flask_cors import CORS

from model.decorators.controller_decorators import requires_login, requires_roles
from model.enum.role import Role
from model.request.user_login_request import UserLoginRequest
from model.request.user_register_request import UserRegisterRequest
from service.session_service import SessionService
from service.user_service import UserService

user_service = UserService()
session_service = SessionService()

user_controller = Blueprint('authentication', __name__, url_prefix='/authentication')
CORS(user_controller, supports_credentials=True)


@user_controller.route('/register', methods=["POST"])
def register_user():
    user_request = UserRegisterRequest(request.json)
    user = user_service.register(user_request)
    return "User '" + str(user.name) + "' correctly registered"


@user_controller.route("/login", methods=["POST"])
def login():
    print(session)
    login_request = UserLoginRequest(request.json)
    user_service.login(login_request)
    print(session)
    return jsonify(session_service.current_user())


@user_controller.route("/logout", methods=["POST"])
@requires_login
def logout():
    return "User '" + user_service.logout().username + "' correctly logged out"


@user_controller.route("/current-user")
@requires_login
def current_user():
    print(session)
    user = session_service.current_user()
    if user:
        return jsonify(user)
    return "User not found", 404


@user_controller.route("/test")
@requires_roles([Role.ADMIN])
@requires_login
def test():
    return "Nice, you have logged and you have the ADMIN role, nicele"
