import logging
import re

from curl_to_swagger.model.model import UrlModel
from curl_to_swagger.service.services import UrlService

logger = logging.getLogger(f'c2s.{__name__}')


class UrlServiceImpl(UrlService):

    def __init__(self):
        pass

    def create_url(self, payload_model: UrlModel):
        url = payload_model.url
        path = re.split('^[vV][0-9]+', url)
        # split url in order to retrieve server
        # split url in order to retrieve path
        pass
