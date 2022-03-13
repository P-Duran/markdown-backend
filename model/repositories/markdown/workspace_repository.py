from model.repositories.mongo_repository import MongoRepository, collection


@collection("markdown")
class MarkdownRepository(MongoRepository):
    pass

