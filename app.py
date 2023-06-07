from flask import request, jsonify
from config import app, api
from api import QuizClient
from models import QuizQuestion
from flask_restful import Resource
from marshmallow import ValidationError

api_client = QuizClient()


@app.route('/api/quiz/testexisted', methods=['POST'])
def test_existed_question():
    data = [request.get_json()]
    res = False
    while res is False:
        res = QuizQuestion.insert_data(data)
        data = api_client.get_new_questions(count=1)
    return jsonify([i_question for i_question in QuizQuestion.get_prev_data()])


class Quiz(Resource):
    def post(self):
        res = False
        request_data = request.json
        questions_count = request_data.get('questions_count')
        if not questions_count:
            return 'Не указан параметр [questions_count]', 400
        while res is False:
            data = api_client.get_new_questions(count=questions_count)
            print(data)
            res = QuizQuestion.insert_data(data)
        return jsonify([i_question for i_question in QuizQuestion.get_prev_data()])

    def get(self):
        return jsonify(
            [i_question.to_json() for i_question in QuizQuestion.get_all_questions()]
        )


api.add_resource(Quiz, '/api/quiz')

if __name__ == '__main__':
    with app.app_context():
        QuizQuestion.delete_all()
    app.run()
