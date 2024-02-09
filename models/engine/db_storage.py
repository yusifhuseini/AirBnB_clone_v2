#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
=======

"""
A module that defines extensively the database storage for this project
"""
from os import getenv
from models.base_model import Base
from models.user import User
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

=======
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Database utilities definition"""
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
=======
        """Instantiation method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Makes a query to the database
        if cls is given, query for cls only else query for all"""
        objs = []
        if cls is None:
            Classes = [User, City, State, Place, Review, Amenity]
            try:
                for Class in Classes:
                    objs = objs + self.__session.query(Class).all()
            except Exception:
                pass
        else:
            Class = eval(cls) if type(cls) == str else cls
            objs = self.__session.query(Class).all()
        return {'{}.{}'.format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
<<<<<<< HEAD
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
=======
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
<<<<<<< HEAD
        """Close the working SQLAlchemy session."""
=======
        """Dispose of the current Session, if present."""
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
        self.__session.close()
