import json
from unittest import TestCase
from unittest.mock import Mock

from curl_to_swagger.service.body_service import BodyServiceImpl


class TestBodyServiceImpl(TestCase):

    def setUp(self):
        self._body_repository = Mock()

    def test_create_body(self):
        body_service = BodyServiceImpl(self._body_repository)
        base64_body = 'LS1kYXRhLXJhdyAneyJvcmRlciI6eyJpdGVtcyI6W3sicHJvZHVjdElkIjoiODczYjk5OTQtZDkxZC00NTdlLTgzYmItOTI2YTc4Mjk5ZmQ4In1dfX0n'
        body_service.create_body(base64_body)
        expected = json.dumps('{"order":{"items":[{"productId":"873b9994-d91d-457e-83bb-926a78299fd8"}]}}')
        self._body_repository.persist.assert_called_with(expected)
