import base64
import logging

from curl_to_swagger.service.services import HeaderService

logger = logging.getLogger(f'c2s.{__name__}')


class HeaderRepository:
    def create(self, headers: dict):
        pass


class HeaderServiceImpl(HeaderService):

    def __init__(self, header_repository: HeaderRepository):
        self._header_repository = header_repository

    def create_header(self, base64_headers: str):
        message = base64.b64decode(base64_headers).decode('utf-8')
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
