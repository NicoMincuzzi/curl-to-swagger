import base64
import json
import logging

from curl_to_swagger.model.model import BodyModel
from curl_to_swagger.service.services import BodyService

logger = logging.getLogger(f'c2s.{__name__}')


class BodyRepository:
    def persist(self, endpoint_id: str, body: str):
        pass


class BodyServiceImpl(BodyService):

    def __init__(self, body_repository: BodyRepository):
        self._body_repository = body_repository

    def create_body(self, body_model: BodyModel):
        if not body_model.payload:
            return
        message = base64.b64decode(body_model.payload).decode('utf-8')
        message = message.replace('\'', '').replace(' ', '').split('--data-raw')
        message.remove('')
        self._body_repository.persist(body_model.id, json.dumps(message[0]))
