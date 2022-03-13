from datetime import datetime
from model.repositories.mongo_document import MongoDocument

class WorkspaceDocument(MongoDocument):
    user: str = None
    createdAt: datetime = None
    updatedAt: datetime = None



