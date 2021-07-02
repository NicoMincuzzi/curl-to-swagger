import logging

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.service.services import UrlService

logger = logging.getLogger(f'c2s.{__name__}')


class UriRepository:
    def persist(self, uri: dict) -> str:
        pass


class UrlServiceImpl(UrlService):

    def __init__(self, uri_repository: UriRepository):
        self._uri_repository = uri_repository

    def create_url(self, uri_model: UriModel) -> str:
        protocol, url = uri_model.uri.split('://')
        temp_dict = {'httpMethod': uri_model.http_method,
                     'protocol': protocol,
                     'domain': (url.split('/')[0]),
                     'resource': (url.replace(url.split('/')[0], ''))
                     }
        return self._uri_repository.persist(temp_dict)
