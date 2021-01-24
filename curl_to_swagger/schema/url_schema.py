from marshmallow import fields, post_load

from curl_to_swagger.model.model import UrlModel
from curl_to_swagger.schema.base_schema import BaseSchema


class UrlSchema(BaseSchema):
    http_method = fields.String(data_key='httpMethod', required=True)
    url = fields.String(data_key='url', required=True)

    @post_load
    def make_model(self, data):
        return UrlModel(**data)
