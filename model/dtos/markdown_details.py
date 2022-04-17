from datetime import datetime

from model.repositories.mongo_document import MongoDocument


class MarkdownDetails(MongoDocument):
    name: str = None
    user: str = None
    pages: int = None
    preview: str = None
    createdAt: datetime = None
    updatedAt: datetime = None