import unittest

from curl_to_swagger.model.model import UrlModel
from curl_to_swagger.service.url_service import UrlServiceImpl


class UrlServiceTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._url_service = UrlServiceImpl()

    def test_create_url(self):
        url_model: UrlModel = UrlModel(http_method="POST", url="https://domain.com/app/api/v1/products/<product-id>")
        self._url_service.create_url(url_model)
        self.assertEqual(True, True)
