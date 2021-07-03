from marshmallow import fields, post_load

from curl_to_swagger.model.model import UriModel
from curl_to_swagger.schema.base_schema import BaseSchema


class UriSchema(BaseSchema):
    http_method = fields.String(data_key='httpMethod', required=True)
    uri = fields.String(data_key='uri', required=True)

    @post_load
    def make_model(self, data):
        return UriModel(**data)
