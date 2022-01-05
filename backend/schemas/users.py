from typing import Optional
from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    password: str
    mail: str


class ShowUser(BaseModel):
    id: int
    username: str
    hash_password: str
    mail: str
    disabled: bool

    class Config:
        orm_mode = True
