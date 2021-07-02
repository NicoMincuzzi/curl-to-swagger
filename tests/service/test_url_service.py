from unittest import TestCase
from unittest.mock import Mock

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.service.services import UrlService
from curl_to_swagger.service.url_service import UrlServiceImpl


class TestUrlServiceImpl(TestCase):

    def setUp(self) -> None:
        self._uri_repository = Mock()
        self._urlService: UrlService = UrlServiceImpl(self._uri_repository)

    def test_create_url(self):
        uri = UriModel(uri='https://it.test.com/service/api/v2/products/b43e508d-ef45-4c15-97ac-ed468ad5bcdc',
                       http_method='GET')
        self._urlService.create_url(uri)
        expected = {'httpMethod': 'GET', 'protocol': 'https', 'domain': 'it.test.com',
                    'resource': '/service/api/v2/products/b43e508d-ef45-4c15-97ac-ed468ad5bcdc'}
        self._uri_repository.persist.assert_called_once_with(expected)

    def test_create_url_no_specific_http_method(self):
        uri = UriModel(uri='https://it.test.com/service/api/v2/products/b43e508d-ef45-4c15-97ac-ed468ad5bcdc')
        self._urlService.create_url(uri)
        expected = {'httpMethod': 'GET', 'protocol': 'https', 'domain': 'it.test.com',
                    'resource': '/service/api/v2/products/b43e508d-ef45-4c15-97ac-ed468ad5bcdc'}
        self._uri_repository.persist.assert_called_once_with(expected)
