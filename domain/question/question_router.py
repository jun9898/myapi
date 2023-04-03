from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database import SessionLocal

from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list(db: Session = Depends(get_db)):  #FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.

    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # db.close() ----------- database에 작업이 시작되면 세션을 열어주고 완료되면 자동으로 세션을 닫아주는 get_db 함수를 등록하여 코드 작성 마지막에 db.close()를 입력하지 않아도 됩니다.

    # with get_db() as db: # db 세션 객체를 사용한다.

    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list