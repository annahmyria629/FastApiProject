import enum
from sqlalchemy import Boolean, Column, Integer, String, Enum
from backend.db.base_class import Base
from backend.auth.jwt import get_hashed_password


class Role(enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, primary_key=True, unique=True, nullable=False)
    hash_password = Column(String, primary_key=True, nullable=False)
    mail = Column(String, unique=True)
    role = Column(Enum(Role), default=Role.user)
    # role = Column(String, default="user")
    disabled = Column(Boolean, default=False)

    def __init__(self, username, password, mail, role="user", disabled=False):
        self.username = username
        self.hash_password = get_hashed_password(password)
        self.mail = mail
        self.role = Role[role.lower()]
        self.disabled = disabled
