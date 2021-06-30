import logging

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.service.services import UrlService

logger = logging.getLogger(f'c2s.{__name__}')


class UriRepository:
    def persist(self, uri: dict):
        pass


class UrlServiceImpl(UrlService):

    def __init__(self, uri_repository: UriRepository):
        self._uri_repository = uri_repository

    def create_url(self, uri_model: UriModel):
        url = uri_model.url
        temp_dict = {}
        self._uri_repository.persist(temp_dict)
        # path = re.split('^[vV][0-9]+', url)
        # split url in order to retrieve server
        # split url in order to retrieve path
