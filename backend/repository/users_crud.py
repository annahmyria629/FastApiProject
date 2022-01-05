from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

from backend.schemas.users import CreateUser
from backend.db.models.users import User

from backend.auth.jwt import get_hashed_password


def create_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        mail=user.mail,
        password=get_hashed_password(user.password),
        role="user",
        disabled=False
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        db.rollback()
        raise Exception("Such user has already existed")
