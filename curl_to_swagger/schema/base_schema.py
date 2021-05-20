import logging

from marshmallow import Schema, post_dump, missing

logger = logging.getLogger(f'c2s.{__name__}')


class BaseSchema(Schema):
    class Meta:
        ordered = True
        strict = True

    @staticmethod
    def on_bind_field(field_obj):
        if field_obj.missing == missing:
            field_obj.missing = None
            field_obj.allow_none = True

    @post_dump
    def clean_missing(self, data):
        ret = data.copy()
        for key in filter(lambda _key: data[_key] is None, data):
            del ret[key]
        return ret

    @staticmethod
    def handle_error(error, data):
        logger.debug(f'Cannot validate input: {data}')
        logger.warning(f'Validation error: {error.messages}')
