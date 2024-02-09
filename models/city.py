#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
=======

"""
A module that defines the ORM class for City table
"""
from os import getenv
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
<<<<<<< HEAD
    """Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
=======
    """
    The city class, contains state ID and name
    """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            'Place', backref='cities', cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
