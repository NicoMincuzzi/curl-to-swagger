import logging

from injector import Module, Binder, singleton

from curl_to_swagger.service.converter_service import ConverterServiceImpl
from curl_to_swagger.service.services import ConverterService

logger = logging.getLogger(f'c2s.{__name__}')


class ConfigurationModule(Module):

    def configure(self, binder: Binder) -> None:
        pass


class CurlToSwaggerModule(Module):

    def __init__(self):
        logger.info('Configuration cUrl2Swagger injection module...')

    def configure(self, binder: Binder) -> None:
        binder.bind(interface=ConverterService, to=ConverterServiceImpl, scope=singleton)