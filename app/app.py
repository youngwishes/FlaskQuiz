from flask import request, jsonify, Response
from config import app, api
from api import QuizClient
from models import QuizQuestion
from flask_restful import Resource
from schemas import QuizSchema
from marshmallow import ValidationError

api_client = QuizClient()


@app.route('/api/quiz/testexisted', methods=['POST'])
def test_existed_question():
    schema = QuizSchema()
    data = [request.get_json()]
    was_added = False
    while was_added is False:
        try:
            schema.load(data, many=True)
        except ValidationError as exc:
            return exc.messages, 400
        else:
            was_added = QuizQuestion.insert_data(data)
        data = api_client.get_new_questions(count=1)
    return jsonify([i_question for i_question in QuizQuestion.get_prev_data()])


class Quiz(Resource):
    schema = QuizSchema()

    def post(self):
        was_added = False
        questions_count = request.json.get('questions_count')
        if not questions_count:
            return 'Please specify a <questions_count> parameter', 400
        while not was_added:
            data = api_client.get_new_questions(count=questions_count)
            try:
                self.schema.load(data, many=True)
            except ValidationError as exc:
                print(exc.messages)
            else:
                was_added = QuizQuestion.insert_data(data)
        return jsonify([i_question for i_question in QuizQuestion.get_prev_data()])

    def get(self):
        return jsonify(
            [i_question.to_json() for i_question in QuizQuestion.get_all_questions()]
        )


api.add_resource(Quiz, '/api/quiz')

if __name__ == '__main__':
    with app.app_context():
        QuizQuestion.delete_all()
    app.run(host="0.0.0.0")
