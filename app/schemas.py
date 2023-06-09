from marshmallow import Schema, fields, validates, ValidationError
from models import QuizQuestion


class QuizSchema(Schema):
    id = fields.Integer(required=True)
    question = fields.String(required=True)
    answer = fields.String(required=True)
    created_at = fields.String(required=True)

    @validates('id')
    def validate_id(self, id: int) -> None:
        if QuizQuestion.get_by_id(id=id):
            raise ValidationError(
                'Question with id {qid} already exists'.format(qid=id)
            )
