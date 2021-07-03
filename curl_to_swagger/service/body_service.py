import base64
import json
import logging

from curl_to_swagger.service.services import BodyService

logger = logging.getLogger(f'c2s.{__name__}')


class BodyRepository:
    def persist(self, body):
        pass


class BodyServiceImpl(BodyService):

    def __init__(self, body_repository: BodyRepository):
        self._body_repository = body_repository

    def create_body(self, base64_body: str):
        message = base64.b64decode(base64_body).decode('utf-8')
        message = message.replace('\'', '').replace(' ', '').split('--data-raw')
        message.remove('')
        self._body_repository.persist(json.dumps(message[0]))
