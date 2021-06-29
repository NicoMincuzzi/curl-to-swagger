from unittest import TestCase
from unittest.mock import Mock

from curl_to_swagger.service.header_service import HeaderServiceImpl
from curl_to_swagger.service.services import HeaderService


class TestHeaderServiceImpl(TestCase):

    def setUp(self):
        self._header_repository = Mock()
        self._header_service: HeaderService = HeaderServiceImpl(self._header_repository)

    def test_create_header(self):
        base64_headers = 'LUggJ2F1dGhvcml0eTogaXQudGVzdC5jb20nIC1IICdhY2NlcHQtbGFuZ3VhZ2U6IGl0Jw=='
        self._header_service.create_header(base64_headers)
        self._header_repository.create.assert_called_with({'authority': 'it.test.com', 'accept-language': 'it'})
