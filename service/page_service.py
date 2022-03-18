import datetime
import uuid
from http import HTTPStatus
from typing import List, Optional

from flask import abort, Response

from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.page.page_document import PageDocument
from model.repositories.page.page_repository import PageRepository
from service.markdown_service import MarkdownService
from service.session_service import SessionService


class PageService(metaclass=SingletonMeta):
    page_repository = PageRepository()
    markdown_service = MarkdownService()
    session_service = SessionService()

    def find_all(self) -> List[PageDocument]:
        return [PageDocument(doc) for doc in self.page_repository.find({})]

    def find_by_id(self, id) -> Optional[PageDocument]:
        result = [PageDocument(doc) for doc in self.page_repository.find({"_id": id})]
        if len(result) > 0:
            return result[0]
        return None

    def find_all_by_workspace(self, markdown: str) -> List[PageDocument]:
        return [PageDocument(doc) for doc in self.page_repository.find({"markdown": markdown})]

    def find_all_with_query(self, query: dict) -> List[PageDocument]:
        return [PageDocument(doc) for doc in self.page_repository.find(query)]

    def save(self, document: PageDocument):
        now = datetime.datetime.now()
        current_user = self.session_service.current_user()
        if document.id is None or self.find_by_id(document.id) is None:
            document = document.copy_with(_id=str(uuid.uuid4()), createdAt=now, updatedAt=now, user=current_user.name)
            if not self.markdown_service.find_by_id(document.markdown):
                abort(Response("Markdown with id '" + str(document.markdown) + "' not found",
                               status=HTTPStatus.NOT_FOUND))
        else:
            document = document.copy_with(updatedAt=now)
        self.page_repository.save(document)
        return PageDocument(document)

    def delete_all_by_markdown(self, markdown):
        self.page_repository.delete_all({"markdown": markdown})

    def delete(self, id) -> Optional[PageDocument]:
        deleted_item = self.find_by_id(id)
        self.page_repository.delete(id)
        return deleted_item
