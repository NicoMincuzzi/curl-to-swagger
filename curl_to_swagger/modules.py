import logging

from injector import Module, Binder, singleton

from curl_to_swagger.service.body_service import BodyServiceImpl
from curl_to_swagger.service.header_service import HeaderServiceImpl
from curl_to_swagger.service.services import UrlService, HeaderService, BodyService, SwaggerService
from curl_to_swagger.service.swagger_service import SwaggerServiceImpl
from curl_to_swagger.service.url_service import UrlServiceImpl

logger = logging.getLogger(f'c2s.{__name__}')


class ConfigurationModule(Module):

    def configure(self, binder: Binder) -> None:
        pass


class CurlToSwaggerModule(Module):

    def __init__(self):
        logger.info('Configuration cUrl2Swagger injection module...')

    def configure(self, binder: Binder) -> None:
        binder.bind(interface=SwaggerService, to=SwaggerServiceImpl, scope=singleton)
        binder.bind(interface=UrlService, to=UrlServiceImpl, scope=singleton)
        binder.bind(interface=HeaderService, to=HeaderServiceImpl, scope=singleton)
        binder.bind(interface=BodyService, to=BodyServiceImpl, scope=singleton)
