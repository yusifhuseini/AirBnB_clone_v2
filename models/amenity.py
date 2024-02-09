#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
=======

"""
A module that defines the ORM class for Amenity table
"""
from os import getenv
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
=======
    """
    Defines Amenity class attributes
    """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(60), nullable=False)
        place_amenities = relationship(
            'Place', secondary=place_amenity, viewonly=False
        )
    else:
        name = ''
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
