from marshmallow import Schema, fields


class QuizSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    created_at = fields.Date(required=True)
