from datetime import datetime

from model.enum.role import Role
from model.repositories.mongo_document import MongoDocument

class UserDocument(MongoDocument):
    name: str = None
    email: str = None
    password = None
    role: Role = None
    createdAt: datetime = None
    updatedAt: datetime = None



