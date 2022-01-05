from fastapi import FastAPI, Body, Header, File, Depends, HTTPException, APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from backend.schemas.users import CreateUser, ShowUser
from backend.db.models.users import User
# from backend.app.models.author import Author
# from backend.app.auth.jwt import auth_user, generate_jwt, get_hashed_password

from sqlalchemy.orm import Session
from backend.db.session import get_db

# from ..db.database import SessionLocal, engine
# from backend.db.schemas import User
# from ..db import schemas

from .route_users import user_router

app_v1 = APIRouter(
    prefix="/v1"
)

app_v1.include_router(user_router)
# oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
# schemas.Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get("/")
# async def hello_world():
#     return {"hello"}

# to run server: uvicorn run:app --reload --port 8001


# @app_v1.post("/token")
# async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     username = form_data.username
#     password = form_data.password
#     if auth_user(username, password):
#         return {"token": generate_jwt(username)}
#     else:
#         raise HTTPException(HTTP_401_UNAUTHORIZED)




# # /user?login
# @app_v1.get("/user")
# async def get_user(username: str):
#     return {"username": username}
#
#
# @app_v1.get("/book/{isbn}")
# async def get_book_with_isbn(isbn: str):
#     return {"isbn": isbn}
#
#
# @app_v1.get("/author/{id}/book")
# async def get_aothors_books(id: int, category: str, order: str = "asc"):
#     return {"isbn": str(id) + category + order}
#
#
# # name: str = Body(...) means that name will come from json
# @app_v1.patch("/author/name")
# async def patch_author_name(name: str = Body(..., embed=True)):
#     return {"name": name}
#
#
# # if we need to get param from body and this param is not out object - test_param: str = Body(..., embed=True)
# # input json:
# # {
# #     "user":{
# #             "username": "username",
# #             "password": "pwd",
# #             "mail": "email",
# #             "role": "admin"
# #     },
# #     "author":{
# #         "name": "n",
# #         "books_list":[1]
# #     },
# #     "test_param":"tmp"
# #
# # }
# #
# # custom_header: str = Header("default") - to get custom header from request headers
# @app_v1.post("/user/author", response_model=User,
#           response_model_exclude={"password"}, status_code=HTTP_201_CREATED)
# async def test_endpoint(user: User, author: Author, test_param: str = Body(..., embed=True),
#                         custom_header: str = Header("default")):
#     items = {
#         "username": "usr",
#         "password": "pwd",
#         "mail": "my_mail",
#         "role": "user"
#     }
#     return User(**items)
#     # return {"user": user, "author": author, "test_param": test_param, "custom_header": custom_header}
#
#
# #file to upload endpoint
# @app_v1.post("/user/photo")
# async def upload_photo(response: Response, profile_photo: bytes = File(...)):
#     response.headers["x-file-size"] = str(len(profile_photo))
#     response.set_cookie(key="my_cookie", value="t")
#     return {"size": len(profile_photo)}
