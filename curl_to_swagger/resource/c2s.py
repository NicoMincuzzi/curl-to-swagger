import json

from flask import Response
from flask_restful import Resource
from injector import inject


class SwaggerResource(Resource):

    @inject
    def __init__(self, body_service: BodyService):
        self._body_service = body_service

    def get(self, endpoint_id):
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')
