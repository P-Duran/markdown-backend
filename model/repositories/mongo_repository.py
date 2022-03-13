import os
from pymongo import MongoClient
from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.mongo_document import MongoDocument


class MongoRepository(metaclass=SingletonMeta):
    database = None
    def __init__(self, collection):
        db = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                         port=27017,
                         username=os.environ['MONGODB_USERNAME'],
                         password=os.environ['MONGODB_PASSWORD'],
                         authSource=os.environ['MONGODB_DATABASE'])
        self.database = db[os.environ['MONGODB_DATABASE']][collection]

    def find_all(self):
        return self.database.find()

    def find_by_id(self, id):
        return self.database.find({"_id": id})

    def find(self, query: dict):
        return self.database.find(query)

    def find_one(self, query: dict):
        return self.database.find_one(query)

    def save(self, document: MongoDocument):
        return self.database.update_one({'_id':document.id}, {"$set": document}, upsert = True)

    def delete(self, id):
        return self.database.delete_one({'_id': id})

    def delete_all(self, query):
        return self.database.delete_many(query)


#--------------DECORATOR--------------
# function returning a decorator, takes arguments
def collection(collection):
    # this does the actual heavy lifting of decorating the class
    # it takes the original class, modifies it in place, and returns
    # the same class
    def wrapper(wrapped):
        the_init = wrapped.__init__

        def new_init(self):
            super(self.__class__, self).__init__(collection)
            the_init(self, collection)

        wrapped.__init__ = new_init

        return wrapped
    return wrapper