from model.repositories.mongo_repository import MongoRepository, collection


@collection("user")
class UserRepository(MongoRepository):

    def save(self, document):
        self.database.create_index([("username", 1), ("email", 1)], unique = True)
        super(UserRepository, self).save(document)

