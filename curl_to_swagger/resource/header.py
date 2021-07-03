import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.service.services import HeaderService


class HeaderResource(Resource):

    @inject
    def __init__(self, header_service: HeaderService):
        self._header_service = header_service

    def post(self):
        data = request.get_json()
        self._header_service.create_header()
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')
