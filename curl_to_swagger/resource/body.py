import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.model.model import BodyModel
from curl_to_swagger.schema.body_schema import BodySchema
from curl_to_swagger.service.services import BodyService


class BodyResource(Resource):

    @inject
    def __init__(self, body_service: BodyService):
        self._body_service = body_service

    def post(self):
        body_model: BodyModel = BodySchema().load(request.get_json())
        self._body_service.create_body(body_model)
        response = json.dumps({'id': 'endpoint creato'})
        return Response(status=201, response=response, mimetype='application/json')
