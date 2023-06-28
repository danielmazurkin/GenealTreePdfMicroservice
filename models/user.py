from config.base import Base
from sqlalchemy import Column, Integer, String, Enum
from models.enums import UserRoleEnum


class User(Base):
    """Модель пользователя."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role_user = Column(Enum(UserRoleEnum), default=UserRoleEnum.viewer)
    tree_pk = Column(Integer, primary_key=True, index=True)

    def __str__(self):
        return f"Username = {self.username}"
