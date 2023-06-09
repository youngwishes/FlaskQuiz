FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y libpq-dev build-essential

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --upgrade pip && python -m pip install -r requirements.txt

COPY app /usr/src/app

ENV SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://flaskquiz:12345@localhost:5432/flaskquiz"

EXPOSE 5000
