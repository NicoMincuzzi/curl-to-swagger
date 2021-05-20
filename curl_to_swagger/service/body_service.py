import logging

from curl_to_swagger.model.model import UrlModel
from curl_to_swagger.service.services import BodyService

logger = logging.getLogger(f'c2s.{__name__}')


class BodyServiceImpl(BodyService):

    def __init__(self):
        pass

    def create_body(self, payload_model: UrlModel):
        pass
