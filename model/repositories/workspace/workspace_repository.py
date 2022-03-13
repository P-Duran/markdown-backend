from model.repositories.mongo_repository import MongoRepository, collection


@collection("workspace")
class WorkspaceRepository(MongoRepository):
    pass

