import datetime
import uuid
from typing import List, Optional

from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.markdown.markdown_document import MarkdownDocument
from model.repositories.markdown.workspace_repository import MarkdownRepository
from service.session_service import SessionService


class MarkdownService(metaclass=SingletonMeta):
    markdown_repository = MarkdownRepository()
    session_service = SessionService()

    def find_with_query(self, query: dict):
        return [MarkdownDocument(doc) for doc in self.markdown_repository.find(query)]

    def delete_with_query(self, query: dict):
        result = self.find_with_query(query)
        self.markdown_repository.delete_all(query)
        return result

    def find_all(self) -> List[MarkdownDocument]:
        return [MarkdownDocument(doc) for doc in self.markdown_repository.find_all()]

    def find_by_id(self, id) -> Optional[MarkdownDocument]:
        result = [MarkdownDocument(doc) for doc in self.markdown_repository.find_by_id(id)]
        if len(result) > 0:
            return result[0]
        return None

    def save(self, document: MarkdownDocument):
        now = datetime.datetime.now()
        current_user = self.session_service.current_user()
        if document.id is None or self.find_by_id(document.id) is None:
            document = document.copy_with(_id=str(uuid.uuid4()), createdAt=now, updatedAt=now, user=current_user.name)
        else:
            document = document.copy_with(updatedAt=now)
        self.markdown_repository.save(document)
        return MarkdownDocument(document)

    def delete(self, id) -> Optional[MarkdownDocument]:
        deleted_item = self.find_by_id(id)
        self.markdown_repository.delete(id)
        return deleted_item
