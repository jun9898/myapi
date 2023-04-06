from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database import SessionLocal

from database import get_db
from domain.question import question_schema, question_crud
from starlette import status
# from models import Question --- question_crud를 import해줌으로 따로 Question을 import해줄 필요가 없다.

router = APIRouter(
    prefix="/api/question",
)


# @router.get("/list") question_list 함수의 리턴값은 Question 스키마로 구성된 리스트이다.
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):  #FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.

    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # db.close() ----------- database에 작업이 시작되면 세션을 열어주고 완료되면 자동으로 세션을 닫아주는 get_db 함수를 등록하여 코드 작성 마지막에 db.close()를 입력하지 않아도 됩니다.

    # with get_db() as db: # db 세션 객체를 사용한다.

    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all() --------- 이 코드를 crud파일에 작성하여 Read 작업 코드를 간소화 하였습니다.
    _question_list = question_crud.get_question_list(db) # ----------crud에 작성된 get question list 코로 대체하였습니다.
    return _question_list


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)