#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
=======

"""
A module that defines the ORM class for State table
"""
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
<<<<<<< HEAD
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
=======
    """
    Defines attributes for State table
    """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

        @property
        def cities(self):
            """
            Returns (list): List of City instances
            with state_id equals to the current State.id
            """
            from models.city import City
            from models import storage
            city_list = list(storage.all(City).values())
            return [city for city in city_list if city.state_id == self.id]
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
