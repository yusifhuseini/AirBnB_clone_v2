#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
=======

"""
A module that defines the ORM class for User table
"""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
=======
    """
    Defines attributes for User table
    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'Place', backref='user', cascade='all, delete')
        reviews = relationship(
            'Review', backref='user', cascade='all, delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
