from marshmallow import Schema, post_load
import humps


class BaseSchema(Schema):
    def custom_post_load(self, data, **kwargs):
        return data

    @post_load
    def convert_to_camel_case(self, data, **kwargs):
        return humps.camelize(self.custom_post_load(data, **kwargs))
