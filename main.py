from config.base import Base, engine, SessionLocal
from models.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session


def main():
    """Точка входа в микросервис."""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
