from marshmallow import fields, post_load

from curl_to_swagger.model.model import BodyModel
from curl_to_swagger.schema.base_schema import BaseSchema


class BodySchema(BaseSchema):
    endpoint_id = fields.String(data_key='id', required=True)
    uri = fields.String(data_key='payload')

    @post_load
    def make_model(self, data):
        return BodyModel(**data)
