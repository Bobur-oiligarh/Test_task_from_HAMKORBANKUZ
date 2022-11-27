from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import exc as exceptions
from test_reqres.http_requests.get_users import GetUsers
from models.models import *
from sqlalchemy_utils import database_exists, create_database
Base = declarative_base()

engine = create_engine("sqlite:///database/reqresin_users.db", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

users = GetUsers().response().data.users
for user in users:
    try:
        new_user = User(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email,
                    avatar=user.avatar)
        session.add(new_user)
        session.commit()
    except exceptions:
        print(err)
session.close()
if __name__ == '__main__':
    for user in users:
        print(user.id,
              user.email,
              user.first_name,
              user.last_name,
              user.avatar)
