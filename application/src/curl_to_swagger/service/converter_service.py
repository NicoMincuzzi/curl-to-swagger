import logging

from curl_to_swagger_core.model.model import PayloadModel, CurlModel, SwaggerModel
from curl_to_swagger_core.services import ConverterService

logger = logging.getLogger(f'c2s.{__name__}')


class ConverterServiceImpl(ConverterService):

    def __init__(self):
        pass

    def convert_to_curl(self, payload_model: PayloadModel) -> CurlModel:
        pass

    def convert_to_swagger(self, curl_model: CurlModel) -> SwaggerModel:
        pass
