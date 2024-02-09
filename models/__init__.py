#!/usr/bin/python3
<<<<<<< HEAD
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
=======
"""This module instantiates storage object
@TODOS:
    checks HBNB_TYPE_STORAGE environmental variable to determine storage type
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
"""
from os import getenv
from .user import User
from .city import City
from .place import Place
from .state import State
from .review import Review
from .amenity import Amenity

<<<<<<< HEAD

if getenv("HBNB_TYPE_STORAGE") == "db":
=======
if getenv('HBNB_TYPE_STORAGE') == 'db':
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
