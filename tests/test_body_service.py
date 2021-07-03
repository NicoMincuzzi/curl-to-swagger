import json
from unittest import TestCase
from unittest.mock import Mock

from curl_to_swagger.model.model import BodyModel
from curl_to_swagger.service.body_service import BodyServiceImpl


class TestBodyServiceImpl(TestCase):

    def setUp(self):
        self._body_repository = Mock()

    def test_create_body(self):
        body_service = BodyServiceImpl(self._body_repository)
        base64_body = 'LS1kYXRhLXJhdyAneyJvcmRlciI6eyJpdGVtcyI6W3sicHJvZHVjdElkIjoiODczYjk5OTQtZDkxZC00NTdlLTgzYmItOTI2YTc4Mjk5ZmQ4In1dfX0n'
        body_model = BodyModel(id='1234', payload=base64_body)
        body_service.create_body(body_model)
        expected_payload = json.dumps('{"order":{"items":[{"productId":"873b9994-d91d-457e-83bb-926a78299fd8"}]}}')
        self._body_repository.persist.assert_called_with('1234', expected_payload)

    def test_create_body_no_payload(self):
        body_service = BodyServiceImpl(self._body_repository)
        base64_body = None
        body_model = BodyModel(id='1234', payload=base64_body)
        body_service.create_body(body_model)
        self._body_repository.persist.assert_not_called()

    def test_create_body_empty_payload(self):
        body_service = BodyServiceImpl(self._body_repository)
        base64_body = ''
        body_model = BodyModel(id='1234', payload=base64_body)
        body_service.create_body(body_model)
        self._body_repository.persist.assert_not_called()
