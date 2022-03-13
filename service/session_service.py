from typing import Optional

from flask import session

from model.metaclass.singleton_meta import SingletonMeta
from model.session.user_session import UserSession


class SessionService(metaclass=SingletonMeta):

    def set_user(self, user: UserSession):
        session["user"] = user

    def current_user(self) -> Optional[UserSession]:
        if "user" not in session:
            return None
        return UserSession(session["user"])

    def remove_user(self):
        if "user" in session:
            session.pop("user")