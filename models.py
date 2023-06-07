from config import db
import datetime


class QuizQuestion(db.Model):
    __tablename__ = 'quiz'

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
    def get_ids_set(cls) -> set:
        return set(db.session.query(QuizQuestion.id).all())

    def __repr__(self) -> str:
        return '<Quiz(id={id}, question={qtext})>'.format(id=self.id, qtext=self.question)
