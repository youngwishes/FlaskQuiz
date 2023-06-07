from dataclasses import dataclass
from datetime import date


@dataclass
class Quiz:
    id: int
    question: str
    answer: str
    created_at: date
