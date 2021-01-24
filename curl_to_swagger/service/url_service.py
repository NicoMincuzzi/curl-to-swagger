import logging

from curl_to_swagger.model.model import CurlModel, PayloadModel
from curl_to_swagger.service.services import UrlService

logger = logging.getLogger(f'c2s.{__name__}')


class UrlServiceImpl(UrlService):

    def __init__(self):
        pass

    def create_url(self, payload_model: PayloadModel) -> CurlModel:
        pass
