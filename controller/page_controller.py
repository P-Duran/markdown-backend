from flask import Blueprint, jsonify, request

from model.decorators.controller_decorators import requires_login
from model.repositories.page.page_document import PageDocument
from service.page_service import PageService

page_service = PageService()

page_controller = Blueprint('page', __name__, url_prefix='/page')


@requires_login
@page_controller.route("/")
def get_all_markdown():
    result = page_service.find_all()
    return jsonify(result)


@requires_login
@page_controller.route('/<id>')
def get_markdown_by_id(id):
    result = page_service.find_by_id(id)
    return jsonify(result)


@requires_login
@page_controller.route("/", methods=["POST"])
def post_markdown():
    result = page_service.save(PageDocument(request.json))
    return jsonify(result)


@requires_login
@page_controller.route('/<id>', methods=["DELETE"])
def delete_markdown(id):
    result = page_service.delete(id)
    return jsonify(result)
