from typing import List

from model.dtos.markdown_details import MarkdownDetails
from model.metaclass.singleton_meta import SingletonMeta
from model.repositories.markdown.markdown_document import MarkdownDocument
from model.repositories.page.page_document import PageDocument
from service.markdown_service import MarkdownService
from service.page_service import PageService


class MarkdownDetailsService(metaclass=SingletonMeta):
    markdown_service = MarkdownService()
    page_service = PageService()

    def find_with_query(self, query: dict):
        markdowns = self.markdown_service.find_with_query(query)
        ws_pages = [(markdown, self.page_service.find_all_with_query({"markdown": markdown.id})) for markdown in
                    markdowns]
        return [self.__build_markdown_details__(ws_page[0], ws_page[1]) for
                ws_page in ws_pages]

    def __build_markdown_details__(self, markdown: MarkdownDocument, pages: List[PageDocument]):
        return MarkdownDetails({**markdown, "pages": len(pages), "preview": "" if len(pages) == 0 else pages[0].text})
