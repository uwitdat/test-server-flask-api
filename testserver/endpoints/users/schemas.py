from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta:
        strict = True

    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    date_created = fields.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
