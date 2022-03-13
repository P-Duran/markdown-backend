from flask import Blueprint, jsonify, request

from model.repositories.workspace.workspace_document import WorkspaceDocument
from service.workspace_service import WorkspaceService

workspace_service = WorkspaceService()

workspace_controller = Blueprint('workspace', __name__, url_prefix='/workspace')


@workspace_controller.route("/")
def get_all_workspace():
    result = workspace_service.find_all()
    return jsonify(result)


@workspace_controller.route('/<id>')
def get_workspace_by_id(id):
    result = workspace_service.find_by_id(id)
    return jsonify(result)


@workspace_controller.route("/", methods=["POST"])
def post_markdown():
    result = workspace_service.save(WorkspaceDocument(request.json))
    return jsonify(result)


@workspace_controller.route('/<id>', methods=["DELETE"])
def delete_markdown(id):
    result = workspace_service.delete(id)
    return jsonify(result)
