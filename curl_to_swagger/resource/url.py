import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.schema.url_schema import UrlSchema
from curl_to_swagger.service.services import UrlService


class UrlResource(Resource):

    @inject
    def __init__(self, url_service: UrlService):
        self._url_service = url_service

    def post(self):
        endpoint_model: UriModel = UrlSchema().load(request.get_json())
        self._url_service.create_url(url_model=endpoint_model)
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')

    def get(self):
        data = request.get_json()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=200, response=response, mimetype='application/json')

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
