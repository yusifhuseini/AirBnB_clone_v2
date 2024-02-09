#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table reviews.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
=======

"""
A module that defines ORM class for Review table
"""
from os import getenv
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """
    Defines attributes for Review table
    """
    __tablename__ = 'reviews'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ''
        place_id = ''
        user_id = ''
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
