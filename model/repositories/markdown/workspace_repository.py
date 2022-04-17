from model.repositories.mongo_repository import MongoRepository, collection
from service.session_service import SessionService


@collection("markdown")
class MarkdownRepository(MongoRepository):
    session_service = SessionService()

    def find(self, query: dict):
        return super(MarkdownRepository, self).find(self.__inject_restriction__(query))

    def find_one(self, query: dict):
        return super(MarkdownRepository, self).find_one(self.__inject_restriction__(query))

    def delete(self, id):
        return super(MarkdownRepository, self).delete_one(self.__inject_restriction__({"_id": id}))

    def __inject_restriction__(self, query: dict) -> dict:
        return {**query, "user": self.session_service.current_user().name}
