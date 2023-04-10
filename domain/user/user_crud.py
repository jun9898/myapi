from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    db.commit()
    #database.User 객체에 사용자가 입력한 정보는 add 한 뒤 commit 하는 코드이다


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()