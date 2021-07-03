from marshmallow import fields, post_load

from curl_to_swagger.model.model import HeaderModel
from curl_to_swagger.schema.base_schema import BaseSchema


class HeaderSchema(BaseSchema):
    endpoint_id = fields.String(data_key='id', required=True)
    headers = fields.String(data_key='headers', required=True)

    @post_load
    def make_model(self, data):
        return HeaderModel(**data)
