from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///users.db', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    avatar = Column(String)
    address = relationship("Address", uselist=False, back_populates="user_table")
    contacts = relationship("Contact", back_populates='user')


class Address(Base):
    __tablename__ = "address_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    address = Column(String)


class Contact(Base):
    __tablename__ = "contact_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    phone_number = Column(String)
    user = relationship("User", back_populates='contacts')


