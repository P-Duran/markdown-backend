from flask import Blueprint, jsonify, request

from model.decorators.controller_decorators import requires_login
from model.repositories.markdown.markdown_document import MarkdownDocument
from service.markdown_service import MarkdownService
from service.page_service import PageService

markdown_service = MarkdownService()
page_service = PageService()

markdown_controller = Blueprint('markdown', __name__, url_prefix='/markdown')


@markdown_controller.route("/")
@requires_login
def get_all_workspace():
    result = markdown_service.find_with_query(request.args.to_dict())
    return jsonify(result)


@markdown_controller.route('/<id>')
@requires_login
def get_workspace_by_id(id):
    result = markdown_service.find_by_id(id)
    return jsonify(result)


@markdown_controller.route("/", methods=["POST"])
@requires_login
def post_markdown():
    result = markdown_service.save(MarkdownDocument(request.json))
    return jsonify(result)


@markdown_controller.route('/<id>', methods=["DELETE"])
@requires_login
def delete_markdown(id):
    result = markdown_service.delete(id)
    page_service.delete_all_by_workspace(id)
    return jsonify(result)
