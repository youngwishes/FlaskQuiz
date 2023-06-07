from flask import request, jsonify
from config import app, api
from api import QuizClient
from models import QuizQuestion
from flask_restful import Resource, Api

api_client = QuizClient()


class Quiz(Resource):
    def post(self):
        request_data = request.json
        questions_count = request_data.get('questions_count')
        if not questions_count:
            return 'Не указан параметр [questions_count]', 400

        data = api_client.get_new_questions(count=questions_count)
        if not data:
            return {}
        existed_data = QuizQuestion.get_ids_set()
        new_data = []
        for i_question in data.keys() - existed_data:
            new_data.append({'id': i_question, **data.get(i_question)})
        QuizQuestion.insert_data(new_data)
        return jsonify(
            [i_question for i_question in QuizQuestion.get_prev_data()]
        )


api.add_resource(Quiz, '/api/quiz')

if __name__ == '__main__':
    app.run()
