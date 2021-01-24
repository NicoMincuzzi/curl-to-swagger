import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.service.services import BodyService


class BodyResource(Resource):

    @inject
    def __init__(self, body_service: BodyService):
        self._body_service = body_service

    def post(self):
        data = request.get_json()
        self._body_service.create_body()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')

    def get(self, endpoint_id):
        data = request.get_json()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=200, response=response, mimetype='application/json')

    def put(self):
        data = request.get_json()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=204, response=response, mimetype='application/json')

    def patch(self):
        data = request.get_json()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=204, response=response, mimetype='application/json')

    def delete(self):
        data = request.get_json()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')
