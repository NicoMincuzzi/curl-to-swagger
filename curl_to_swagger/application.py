import logging

from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import Injector

from curl_to_swagger.modules import ConfigurationModule, CurlToSwaggerModule
from curl_to_swagger.resource.body import BodyResource
from curl_to_swagger.resource.c2s import SwaggerResource
from curl_to_swagger.resource.url import UrlResource
from curl_to_swagger.resource.header import HeaderResource

logger = logging.getLogger(f'c2s.{__name__}')


class CurlToSwaggerApplication(Flask):
    def __init__(self, injector=None):
        super().__init__(__name__)

        self._api = CurlToSwaggerApi(self)
        self._api.add_resource(SwaggerResource, '/', endpoint='')
        self._api.add_resource(UrlResource, '/', endpoint='endpoints')
        self._api.add_resource(HeaderResource, '/', endpoint='headers')
        self._api.add_resource(BodyResource, '/', endpoint='bodies')

        if not injector:
            injector = Injector(modules=[ConfigurationModule(), CurlToSwaggerModule()])
        FlaskInjector(app=self, injector=injector)


class CurlToSwaggerApi(Api):
    def __init__(self, application):
        super().__init__(app=application, prefix='/api/v1/c2s')
        logger.info(f'cURL2Swagger API running (prefix: {self.prefix}).')
