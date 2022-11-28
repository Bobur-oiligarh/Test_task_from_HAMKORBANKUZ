from sqlalchemy import exc
from sqlalchemy_utils import database_exists, create_database
from database.models.models import User, Address, Contact
from database.db_tools.base import Session, engine, Base
from test_reqres.http_requests.get_users import GetUsers

Base.metadata.create_all(engine)
session = Session()

user_objects = GetUsers().response().data.users

if not database_exists(engine.url):
    create_database(engine.url)

for user_obj in user_objects:
    # Check if user exists in db
    user = (
        session.query(User).filter(User.first_name == user_obj.first_name,
                                   User.last_name == user_obj.last_name).one_or_none()
    )
    if user is not None:
        continue

    user = User(first_name=user_obj.first_name,
                last_name=user_obj.last_name,
                email=user_obj.email,
                avatar=user_obj.avatar
                )
    try:
        session.add(user)
    except exc.SQLAlchemyError as err:
        session.rollback()
        print(err)

session.commit()

michael = (session.query(User).filter(User.first_name == "Michael")).one_or_none()
lindsay = (session.query(User).filter(User.first_name == "Lindsay")).one_or_none()
tobias = (session.query(User).filter(User.first_name == "Tobias")).one_or_none()
byron = (session.query(User).filter(User.first_name == "Byron")).one_or_none()
george = (session.query(User).filter(User.first_name == "George")).one_or_none()
rachel = (session.query(User).filter(User.first_name == "Rachel")).one_or_none()

# Adding Address to users
michael_addr = Address("Canada, South Dacota, 23", michael)
lindsay_addr = Address("Canada, New Orlean, 67", lindsay)
tobias_addr = Address("Canada, Ontario, 1023", tobias)
byron_addr = Address("USA, San-Fransisko, 3243", byron)
george_addr = Address("USA, Chicago, West Ocland, 2324", george)
rachel_addr = Address("Mexico, New Mexico,  2324", rachel)

# Adding contacts to users
michael_cont = Contact("+9989 91 3245465", michael)
michael_cont_2 = Contact("+998 90 707 77 57", michael)
michael_cont_3 = Contact("+998 33 303 43 34", michael)
lindsay_cont = Contact("+998907523456", lindsay)
tobias_cont = Contact("+998 94 505 55 75", tobias)
byron_cont = Contact("+998908809888", byron)
george_cont = Contact("+99833100 00 07", george)
rachel_cont = Contact("+99899 900 09 07", rachel)

# persist data above
try:
    session.add(michael_addr)
    session.add(lindsay_addr)
    session.add(tobias_addr)
    session.add(byron_addr)
    session.add(george_addr)
    session.add(rachel_addr)

    session.add(michael_cont)
    session.add(michael_cont_2)
    session.add(michael_cont_3)
    session.add(lindsay_cont)
    session.add(tobias_cont)
    session.add(byron_cont)
    session.add(george_cont)
    session.add(rachel_cont)

    session.commit()
except exc.SQLAlchemyError as err:
    session.rollback()
    print(err)
finally:
    session.close()
