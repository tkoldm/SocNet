import json

from bll.TestService import TestService
from flask import Blueprint, Response, jsonify, request, current_app

from .Dto import TestCreateDto
from .TokenHelper import token_required

test_blueprint = Blueprint("test_blueprint", __name__, url_prefix="test")

@test_blueprint.route("/", methods = ['POST'])
def add() -> Response:
    try:
        token_required(request)
        data = request.json
        dto = TestCreateDto(data)
        result = TestService().add(dto.data)
        if type(result) is int:
            return jsonify({'success': f'added test with id {result}'}), 200
        return jsonify({'error': result}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@test_blueprint.route("/<int:id>", methods = ['GET'])
def get_by_id(id: int) -> Response:
    try:
        token_required(request)
        test = TestService().get_by_id(id)
        print(test)
        if test:
            return jsonify({'success': test}), 200
        else:
            return jsonify({'error': 'test not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/", methods = ['GET'])
def get() -> Response:
    try:
        token_required(request)
        page = request.args.get('page', 1, type=int)
        on_page = request.args.get('on_page', int(
            current_app.config['PERSONS_PER_PAGE']), type=int)
        sort_by = request.args.get('sort_by', 'name', type=str)
        result = TestService().get_all(page=page, on_page=on_page, sort_by=sort_by)
        if result:
            return jsonify({'tests': result}), 200
        return jsonify({'error': 'no tests yet'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@test_blueprint.route("/<int:id>", methods = ['PUT'])
#@token_required()
def update(id: int) -> Response:
    token_required(request)
    return 200

@test_blueprint.route("/<int:id>", methods = ['DELETE'])
#@token_required()
def delete(id: int) -> Response:
    token_required(request)
    return 200

@test_blueprint.route("/start/<int:id>", methods = ['GET'])
#@token_required()
def start_test(id: int) -> Response:
    token_required(request)
    return 200

@test_blueprint.route("/check_result/<int:id>", methods = ['POST'])
#@token_required()
def check_result(id: int) -> Response:
    token_required(request)
    return 200
