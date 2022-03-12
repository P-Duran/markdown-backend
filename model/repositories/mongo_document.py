class MongoDocument(dict):
    def __init__(self, dictionary):
        [setattr(self, key, dictionary[key]) for key in dictionary if key in dir(self)]
        super().__init__(self.__dict__)

    def copy_with(self, **kwargs):
        [ __remove_key__(kwargs, key) for key in kwargs.keys() if key not in dir(self)]
        return self.__class__({**self.__dict__, **kwargs})

def __remove_key__(dict, key):
    del dict[key]