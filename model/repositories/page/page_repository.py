from model.repositories.mongo_repository import MongoRepository, collection


@collection("page")
class PageRepository(MongoRepository):
    pass