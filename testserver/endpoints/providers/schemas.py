from marshmallow import Schema, fields


class ProviderSchema(Schema):
    class Meta:
        strict = True

    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    name = fields.Str(required=True)
    date_created = fields.Str()


provider_schema = ProviderSchema()
providers_schema = ProviderSchema(many=True)
