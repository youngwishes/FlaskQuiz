from flask import request
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
        new_questions = QuizQuestion.get_ids_set()

        print(new_questions)
        return 1


api.add_resource(Quiz, '/api/quiz')

if __name__ == '__main__':
    app.run()
