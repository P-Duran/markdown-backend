class MongoDocument(dict):
    def __init__(self, dictionary):
        [setattr(self, key, dictionary[key]) for key in dictionary if key in dir(self)]
        super().__init__(self.__dict__)
