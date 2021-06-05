from marshmallow import fields
from .base_schema import BaseSchema


class DivisionItemSchema(BaseSchema):
    code = fields.String(required=True)
    text = fields.String(required=True)
