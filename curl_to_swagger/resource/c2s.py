import json

from flask import Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.service.services import SwaggerService


class SwaggerResource(Resource):

    @inject
    def __init__(self, swagger_service: SwaggerService):
        self._swagger_service = swagger_service

    def get(self, endpoint_id):
        self._swagger_service.retrieve_swagger(endpoint_id=endpoint_id)
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')
