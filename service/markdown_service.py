import datetime
import uuid
from http import HTTPStatus
from typing import List, Optional

from flask import Response, abort
from model.repositories.markdown.markdown_document import MarkdownDocument
from model.repositories.markdown.markdown_repository import MarkdownRepository
from model.metaclass.singleton_meta import SingletonMeta
from service.user_service import UserService
from service.workspace_service import WorkspaceService


class MarkdownService(metaclass=SingletonMeta):
    markdown_repository = MarkdownRepository()
    workspace_service = WorkspaceService()
    user_service = UserService()

    def find_all(self) -> List[MarkdownDocument]:
       return [MarkdownDocument(doc) for doc in self.markdown_repository.find_all()]

    def find_by_id(self, id) -> Optional[MarkdownDocument]:
        result = [MarkdownDocument(doc) for doc in self.markdown_repository.find_by_id(id)]
        if len(result) > 0:
            return result[0]
        return None

    def find_all_by_workspace(self, workspace: str) -> List[MarkdownDocument]:
        return [MarkdownDocument(doc) for doc in self.markdown_repository.find({"workspace": workspace})]

    def save(self, document: MarkdownDocument):
        now = datetime.datetime.now()
        current_user = self.user_service.current_user()
        if document.id is None or self.find_by_id(document.id) is None:
            document = document.copy_with(_id = str(uuid.uuid4()), createdAt = now, updatedAt = now, user = current_user.name)
            if not self.workspace_service.find_by_id(document.workspace):
                abort(Response("Workspace with id '"+str(document.workspace)+"' not found", HTTPStatus.NOT_FOUND))
        else:
            document = document.copy_with(updatedAt = now)
        self.markdown_repository.save(document)
        return MarkdownDocument(document)

    def delete_all_by_workspace(self, workspace):
        self.markdown_repository.delete_all({"workspace": workspace})

    def delete(self, id) -> Optional[MarkdownDocument]:
        deleted_item = self.find_by_id(id)
        self.markdown_repository.delete(id)
        return deleted_item

