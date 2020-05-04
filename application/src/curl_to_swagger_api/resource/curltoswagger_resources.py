import json

from curl_to_swagger_core.service import ConverterService
from flask import Response
from flask_restful import Resource
from injector import inject


class CurlToSwaggerResource(Resource):

    @inject
    def __init__(self, converter_service: ConverterService):
        self._converter_service = converter_service

    def post(self):
        response = json.dumps({'id': 'helloworld'})
        return Response(status=201, response=response, mimetype='application/json')
