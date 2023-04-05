import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        orm_mode = True # Question 모델의 항목들을 자동으로 Question 스키마로 매핑해준다.


