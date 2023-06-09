FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN apt install -y git

WORKDIR /usr/src/

RUN git init .
RUN git remote add origin https://github.com/777boeing777/FlaskQuiz.git
RUN git pull origin main

RUN pip install --upgrade pip && python -m pip install -r requirements.txt

WORKDIR /usr/src/app/

ENV SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://flaskquiz:12345@localhost:5432/flaskquiz"

EXPOSE 5000
