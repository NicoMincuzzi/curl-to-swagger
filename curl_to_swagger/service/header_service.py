import base64
import logging

from curl_to_swagger.model.model import HeaderModel
from curl_to_swagger.service.services import HeaderService

logger = logging.getLogger(f'c2s.{__name__}')


class HeaderRepository:
    def create(self, headers: dict):
        pass


class HeaderServiceImpl(HeaderService):

    def __init__(self, header_repository: HeaderRepository):
        self._header_repository = header_repository

    def create_header(self, headers_model: HeaderModel):
        message = base64.b64decode(headers_model.headers).decode('utf-8')
        headers_dict = self.build_headers(message)
        self._header_repository.create(headers_dict)

    @staticmethod
    def build_headers(message):
        headers = message.replace('\'', '').replace(' ', '').split('-H')
        headers.remove('')
        headers_dict = {}
        for header in headers:
            k, v = header.split(':')
            headers_dict.update({k: v})
        return headers_dict
