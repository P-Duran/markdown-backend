class MongoDocument(dict):
    _id: str = None

    def __init__(self, dictionary):
        [setattr(self, key, dictionary[key]) for key in dictionary if key in dir(self)]
        super().__init__(self.__dict__)

    def copy_with(self, **kwargs):
        dict_copy = kwargs.copy()
        [ __remove_key__(dict_copy, key) for key in kwargs.keys() if key not in dir(self)]
        return self.__class__({**self.__dict__, **kwargs})

    @property
    def id(self):
        return self._id

def __remove_key__(dict, key):
    del dict[key]