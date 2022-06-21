from datetime import datetime

from model.repositories.mongo_document import MongoDocument

class PageDocument(MongoDocument):
    title: str = None
    text: str = None
    user: str = None
    icon: str = None
    markdown: str = None
    createdAt: datetime = None
    updatedAt: datetime = None



