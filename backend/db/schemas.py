# from sqlalchemy.orm import relationship
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
#
# from .database import Base
#
#
# # class Role(Enum):
# #     __name__ = "role"
# #     user_role = "user"
# #     admin_role = "admin"
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, index=True)
#     username = Column(String, primary_key=True, unique=True, nullable=False)
#     password = Column(String, primary_key=True, nullable=False)
#     mail = Column(String, unique=True)
#     role = Column(Enum("user", "admin", name="Role"), default="user")
#     disabled = Column(Boolean, default=False)