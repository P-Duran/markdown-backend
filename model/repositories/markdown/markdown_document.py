from datetime import datetime
from model.repositories.mongo_document import MongoDocument

class MarkdownDocument(MongoDocument):
    name: str = None
    user: str = None
    createdAt: datetime = None
    updatedAt: datetime = None



