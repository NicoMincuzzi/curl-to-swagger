import json
import unittest
from unittest import TestCase, mock
from unittest.mock import Mock

from flask import Response

from curl_to_swagger.resource.url import UrlResource
from curl_to_swagger.service.services import UrlService


class TestUrlResource(TestCase):

    @unittest.skip
    @mock.patch('curl_to_swagger.resource.url.request')
    def test_post(self, mock_request):
        mock_request.get_json.return_value = json.dumps(
            {'httpMethod': 'GET', 'uri': 'http://it.test.com/service/resource'})
        url_service: UrlService = Mock(return_value='url_entity_id')
        url_resource = UrlResource(url_service)
        result: Response = url_resource.post()
        expected = json.dumps({'id': 'url_entity_id'})
        self.assertEqual(201, result.status)
        # self.assertEqual(expected, result.response)
