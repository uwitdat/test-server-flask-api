from marshmallow import Schema, fields


class ServiceSchema(Schema):
    class Meta:
        strict = True

    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    name = fields.Str(required=True)
    date_created = fields.Str()
    provider_id = fields.Int()


service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
