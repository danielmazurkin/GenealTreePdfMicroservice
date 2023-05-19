from config.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    """Модель пользователя"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def __str__(self):
        return f"Username = {self.username}"
