from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:1234@localhost:5432/bewisetask1'

@app.route('/question', methods=['POST'])
def save_question():
    request_data = request.get_json()
    questions_num = request_data.get('questions_num')
    if questions_num:
        print('OK')
    print(request_data)
    return 'Some answer', 201


if __name__ == '__main__':
    app.run()
