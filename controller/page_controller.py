from flask import Blueprint, jsonify, request
from flask_cors import CORS

from model.decorators.controller_decorators import requires_login
from model.repositories.page.page_document import PageDocument
from service.page_service import PageService

page_service = PageService()

page_controller = Blueprint('page', __name__, url_prefix='/page')
CORS(page_controller, supports_credentials=True)


@page_controller.route("/")
@requires_login
def get_all_markdown():
    result = page_service.find_all_with_query(request.args.to_dict())
    return jsonify(result)


@page_controller.route('/<id>')
@requires_login
def get_markdown_by_id(id):
    result = page_service.find_by_id(id)
    return jsonify(result)


@page_controller.route("/", methods=["POST"])
@requires_login
def post_markdown():
    result = page_service.save(PageDocument(request.json))
    return jsonify(result)


@page_controller.route('/<id>', methods=["DELETE"])
@requires_login
def delete_markdown(id):
    result = page_service.delete(id)
    return jsonify(result)
