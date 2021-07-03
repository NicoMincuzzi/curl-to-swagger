import json

from flask import request, Response
from flask_restful import Resource
from injector import inject

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.schema.url_schema import UriSchema
from curl_to_swagger.service.services import UrlService


class UrlResource(Resource):

    @inject
    def __init__(self, url_service: UrlService):
        self._url_service = url_service

    def post(self):
        endpoint_model: UriModel = UriSchema().load(request.get_json())
        endpoint_id = self._url_service.create_url(url_model=endpoint_model)
        response = json.dumps({'id': endpoint_id})
        return Response(status=201, response=response, mimetype='application/json')
