from datetime import datetime

from model.repositories.mongo_document import MongoDocument

class PageDocument(MongoDocument):
    title: str = None
    markdown: str = None
    user: str = None
    workspace: str = None
    createdAt: datetime = None
    updatedAt: datetime = None



