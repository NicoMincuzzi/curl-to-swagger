import logging

from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import Injector

from curl_to_swagger.modules import ConfigurationModule, CurlToSwaggerModule
from curl_to_swagger_api.resource.curltoswagger_resources import CurlToSwaggerResource

logger = logging.getLogger(f'c2s.{__name__}')


class CurlToSwaggerApplication(Flask):
    def __init__(self, injector=None):
        super().__init__(__name__)

        self._api = CurlToSwaggerApi(self)
        self._api.add_resource(CurlToSwaggerResource, '/', endpoint='curl_to_connect_convert_ep')

        if not injector:
            injector = Injector(modules=[ConfigurationModule(), CurlToSwaggerModule()])
        FlaskInjector(app=self, injector=injector)


class CurlToSwaggerApi(Api):
    def __init__(self, application):
        super().__init__(app=application, prefix='/curl-to-swagger/api/v1')
        logger.info(f'cURL2Swagger API running (prefix: {self.prefix}).')
