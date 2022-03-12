from flask import Blueprint, jsonify, request

from model.repositories.markdown.markdown_document import MarkdownDocument
from service.markdown_service import MarkdownService

markdown_service = MarkdownService()

markdown_controller = Blueprint('markdown', __name__)

@markdown_controller.route('/markdown')
def get_all_markdown():
    result = markdown_service.find_all()
    return jsonify(result)

@markdown_controller.route('/markdown/<id>')
def get_markdown_by_id(id):
    result = markdown_service.find_by_id(id)
    return jsonify(result)

@markdown_controller.route('/markdown', methods = ["POST"])
def post_markdown():
    result = markdown_service.insert_one(MarkdownDocument(request.json))
    return jsonify(result)