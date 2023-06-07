import requests


class QuizClient:
    TIMEOUT: int = 5
    URL: str = 'https://jservice.io/api/random?count=1'

    def __init__(self) -> None:
        self._session = requests.Session()

    def get_new_questions(self, count: int) -> dict:
        response = self._session.get(self.URL, timeout=self.TIMEOUT, params={'count': count})
        questions = {}
        for q in response.json():
            questions[q['id']] = {
                'question': q['question'],
                'answer': q['answer'],
                'created_at': q['created_at']
            }
        return questions
