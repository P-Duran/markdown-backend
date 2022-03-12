import datetime
from typing import List, Optional

from model.repositories.markdown.markdown_document import MarkdownDocument
from model.repositories.markdown.markdown_repository import MarkdownRepository
from model.metaclass.singleton_meta import SingletonMeta


class MarkdownService(metaclass=SingletonMeta):
    markdown_repository = MarkdownRepository()

    def find_all(self) -> List[MarkdownDocument]:
       return [MarkdownDocument(doc) for doc in self.markdown_repository.find_all()]

    def find_by_id(self, id) -> Optional[MarkdownDocument]:
        result = [MarkdownDocument(doc) for doc in self.markdown_repository.find_by_id(id)]
        if len(result) > 0:
            return result[0]
        return None

    def insert_one(self, document: MarkdownDocument):
        new_document = document.copy_with(creationDate = datetime.datetime.now())
        self.markdown_repository.insert_one(new_document)
        return MarkdownDocument(new_document)

