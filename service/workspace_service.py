import datetime
import uuid
from typing import List, Optional
from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.workspace.workspace_document import WorkspaceDocument
from model.repositories.workspace.workspace_repository import WorkspaceRepository
from service.markdown_service import MarkdownService


class WorkspaceService(metaclass=SingletonMeta):
    workspace_repository = WorkspaceRepository()
    markdown_service = MarkdownService()

    def find_all(self) -> List[WorkspaceDocument]:
       return [WorkspaceDocument(doc) for doc in self.workspace_repository.find_all()]

    def find_by_id(self, id) -> Optional[WorkspaceDocument]:
        result = [WorkspaceDocument(doc) for doc in self.workspace_repository.find_by_id(id)]
        if len(result) > 0:
            return result[0]
        return None

    def save(self, document: WorkspaceDocument):
        now = datetime.datetime.now()
        if document.id is None or self.find_by_id(document.id) is None:
            document = document.copy_with(_id = str(uuid.uuid4()), createdAt = now, updatedAt = now)
        else:
            document = document.copy_with(updatedAt = now)
        self.workspace_repository.save(document)
        return WorkspaceDocument(document)

    def delete(self, id) -> Optional[WorkspaceDocument]:
        deleted_item = self.find_by_id(id)
        self.markdown_service.delete_all_by_workspace(id)
        self.workspace_repository.delete(id)
        return deleted_item

