import os
from pymongo import MongoClient
from model.metaclass.singleton_meta import SingletonMeta


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

    def find_by_id(self, _id):
        return self.database.find({"_id": id})

    def insert_one(self, document):
        return self.database.insert_one(document)


#--------------DECORATOR--------------
# function returning a decorator, takes arguments
def collection(collection):
    # this does the actual heavy lifting of decorating the class
    # it takes the original class, modifies it in place, and returns
    # the same class
    def wrapper(wrapped):
        print(dir(wrapped))
        the_init = wrapped.__init__

        def new_init(self):
            print(dir(self))
            super(self.__class__, self).__init__(collection)
            the_init(self, collection)

        wrapped.__init__ = new_init

        return wrapped
    return wrapper