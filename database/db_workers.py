from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import exc as exceptions
from test_reqres.http_requests.get_users import GetUsers
from models.models import *
from sqlalchemy_utils import database_exists, create_database
from database.base import Session, engine, Base


session = Session()


def get_all_users(session: Session):
    try:
        users = (session.query(User).all())
    except Exception:
        print(Exception)
    return users

