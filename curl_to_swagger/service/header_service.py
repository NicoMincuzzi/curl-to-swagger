import logging

from curl_to_swagger.model.model import CurlModel, PayloadModel
from curl_to_swagger.service.services import HeaderService

logger = logging.getLogger(f'c2s.{__name__}')


class HeaderServiceImpl(HeaderService):

    def __init__(self):
        pass

    def create_header(self, payload_model: PayloadModel) -> CurlModel:
        pass
