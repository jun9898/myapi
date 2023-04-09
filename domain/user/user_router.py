from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema

router = APIRouter(
    prefix="/api/user",
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db=db, user_create=_user_create)
    #/create 경로가 입력되었을때 user_schema.UserCreate의 정보를 user_crud.create_user 함수에 의해 db.User에 저장하는 명령어이다.
    #db.User에 저장하기 전 get_existing_user 함수를 이용해 username, email에 중복된 값이 있는지 확인하고 중복된다면 error를 출력하는 작업을 추가하였다.