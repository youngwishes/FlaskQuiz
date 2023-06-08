from typing import Iterable, Any, Dict
from config import db
import datetime


class QuizQuestion(db.Model):
    __tablename__ = 'quiz'

    prev_data = []
    temp_data = []

    def __init__(self, id: int, question: str, answer: str, created_at: datetime) -> None:
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = created_at

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date)

    @classmethod
    def get_by_id(cls, id: int) -> Any:
        return db.session.query(QuizQuestion.id).filter(QuizQuestion.id == id).one_or_none()

    @classmethod
    def add_new_question(cls, data: dict) -> None:
        q = QuizQuestion(**data)
        db.session.add(q)
        db.session.commit()

    @classmethod
    def insert_data(cls, data: Iterable) -> bool:
        db.session.bulk_insert_mappings(QuizQuestion, data)
        cls.mark_data_as_prev(data=data)
        db.session.commit()
        return True

    @classmethod
    def delete_all(cls) -> None:
        db.session.query(QuizQuestion).delete()
        db.session.commit()

    @classmethod
    def mark_data_as_prev(cls, data: Iterable) -> None:
        cls.prev_data = cls.temp_data
        cls.temp_data = data

    @classmethod
    def get_prev_data(cls) -> list:
        return cls.prev_data

    @classmethod
    def get_all_questions(cls) -> list:
        return db.session.query(QuizQuestion).all()

    def __repr__(self) -> str:
        return '<Quiz(id={id}, question={qtext})>'.format(id=self.id, qtext=self.question)

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
