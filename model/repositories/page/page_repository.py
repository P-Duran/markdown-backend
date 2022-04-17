from model.repositories.mongo_repository import MongoRepository, collection
from service.session_service import SessionService


@collection("page")
class PageRepository(MongoRepository):
    session_service = SessionService()

    def find(self, query: dict):
        return super(PageRepository, self).find(self.__inject_restriction__(query))

    def find_one(self, query: dict):
        return super(PageRepository, self).find_one(self.__inject_restriction__(query))

    def delete(self, id):
        return super(PageRepository, self).delete_one(self.__inject_restriction__({"id": id}))

    def __inject_restriction__(self, query: dict) -> dict:
        return {**query, "user": self.session_service.current_user().name}