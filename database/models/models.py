from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from database.base import Base

__all__ = ["User", "Address", "Contact"]


class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    avatar = Column(String)

    def __init__(self, first_name: str, last_name: str, email: str, avatar: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.avatar = avatar


class Address(Base):
    __tablename__ = "address_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    user = relationship("User", backref=backref("address_table", uselist=False))
    address = Column(String)

    def __init__(self, address: str, user):
        self.address = address
        self.user = user


class Contact(Base):
    __tablename__ = "contact_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    phone_number = Column(String)
    user = relationship("User", backref="contact_table")

    def __init__(self, phone_number: str, user: str):
        self.phone_number = phone_number
        self.user = user
