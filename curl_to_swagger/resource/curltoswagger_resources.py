import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.service.services import ConverterService


class CurlToSwaggerResource(Resource):

    @inject
    def __init__(self, converter_service: ConverterService):
        self._converter_service = converter_service

    def post(self):
        data = request.get_json()
        response = json.dumps({'id': 'helloworld'})
        return Response(status=201, response=response, mimetype='application/json')
