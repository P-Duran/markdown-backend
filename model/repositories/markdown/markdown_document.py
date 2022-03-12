from datetime import datetime

from model.repositories.mongo_document import MongoDocument

class MarkdownDocument(MongoDocument):
    id: str = None
    markdown: str = None
    user: str = None
    creationDate: datetime = None
    updateDate: datetime = None



