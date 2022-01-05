from passlib.context import CryptContext
# from backend.app.models.user import User
from datetime import datetime, timedelta
# import backend.app.utils.const as const
import jwt
from backend.core.config import settings
from sqlalchemy.orm import Session
# import time
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from starlette.status import HTTP_401_UNAUTHORIZED
#
pwd_context = CryptContext(schemes=["bcrypt"])
# oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
# jwt_users = [
#     {
#         "username": "user1",
#         "password": "pswd1",
#         "mail": "mail1",
#         "role": "admin"
#     },
#     {
#         "username": "user2",
#         "password": "pswd2",
#         "mail": "mail2",
#         "role": "user"
#     },
#     {
#         "username": "user3",
#         "password": "pswd3",
#         "mail": "mail3",
#         "role": "user"
#     },
# ]
#
# jwt_users_fake_db = [User(**user) for user in jwt_users]
#
#


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# # JWT implementation
#
# Auth user with username and password to give token
def auth_user(username: str, password: str, db: Session):
    if username in [user["username"] for user in jwt_users]:
        index = [user["username"] for user in jwt_users].index(username)
        if verify_password(password, get_hashed_password(jwt_users_fake_db[index].password)):
            return True
    return False
#
#
# Generate jwt
def generate_jwt(username: str):
    jwt_payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_TIME_MINUTES)
    }
    jwt_token = jwt.encode(jwt_payload, settings.JWT_SECRET_KEY, settings.JWT_ALGO)
    return jwt_token
#
#
# # Check if jwt is correct
# def verify_jwt(token: str = Depends(oauth_scheme)):
#     try:
#         jwt_payload = jwt.decode(token, const.JWT_SECRET_KEY, const.JWT_ALGO)
#         username = jwt_payload.get("sub")
#         expiration = jwt_payload.get("exp")
#         if time.time() < expiration:
#             if username in [user["username"] for user in jwt_users]:
#                 return True
#     except Exception as e:
#         raise HTTPException(HTTP_401_UNAUTHORIZED)
#
#     raise HTTPException(HTTP_401_UNAUTHORIZED)