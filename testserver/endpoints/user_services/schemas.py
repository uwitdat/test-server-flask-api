from marshmallow import Schema, fields


class UserServiceSchema(Schema):
    class Meta:
        strict = True

    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    service_id = fields.Int()
    service_name = fields.Str(attribute='name')
    service_description = fields.Str(attribute='description')


user_service_schema = UserServiceSchema()
user_services_schema = UserServiceSchema(many=True)