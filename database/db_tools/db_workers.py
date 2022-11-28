from sqlalchemy import exc
from database.models.models import *


class DBWorker:

    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        try:
            users = self.session.query(User).all()
        except exc.SQLAlchemyError as err:
            error = str(err.__dict__['orig'])
            return error
        return users

    def get_user(self, user_id: int):
        user_obj = None
        try:
            user_obj = self.session.query(User).get(user_id)
        except exc.SQLAlchemyError as err:
            error = str(err.__dict__['orig'])
            return error
        return user_obj

    def get_user_address(self, user_id: int):
        try:
            user_addr_obj = (self.session.query(Address)
                             .join(User).filter(User.id == user_id)
                             .filter(Address.user_id == user_id)
                             ).one_or_none()
            user = user_addr_obj.user
            user_address = user_addr_obj.address
        except exc.SQLAlchemyError as err:
            error = str(err.__dict__['orig'])
            return error
        return user, user_address

    def get_user_contacts(self, user_id):
        try:
            user_contacts_obj = (self.session.query(Contact)
                                 .join(User).filter(User.id == user_id)
                                 .filter(Contact.user_id == user_id)
                                 ).all()
            if user_contacts_obj:
                user = user_contacts_obj[0].user
        except exc.SQLAlchemyError as err:
            error = str(err.__dict__['orig'])
            return error
        return user, user_contacts_obj
