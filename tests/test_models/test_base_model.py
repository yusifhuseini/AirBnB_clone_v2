#!/usr/bin/python3
<<<<<<< HEAD
"""Defines unnittests for models/base_model.py."""
import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """BaseModel testing setup.

        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates a BaseModel instance for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """BaseModel testing teardown.

        Restore original file.json.
        Delete the test BaseModel instance.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.base, BaseModel)

    def test_two_models_are_unique(self):
        """Test that different BaseModel instances are unique."""
        bm = BaseModel()
        self.assertNotEqual(self.base.id, bm.id)
        self.assertLess(self.base.created_at, bm.created_at)
        self.assertLess(self.base.updated_at, bm.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        bm = BaseModel("1", id="5", created_at=dt.isoformat())
        self.assertEqual(bm.id, "5")
        self.assertEqual(bm.created_at, dt)

    def test_str(self):
        """Test __str__ representation."""
        s = self.base.__str__()
        self.assertIn("[BaseModel] ({})".format(self.base.id), s)
        self.assertIn("'id': '{}'".format(self.base.id), s)
        self.assertIn("'created_at': {}".format(repr(self.base.created_at)), s)
        self.assertIn("'updated_at': {}".format(repr(self.base.updated_at)), s)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_save(self):
        """Test save method."""
        old = self.base.updated_at
        self.base.save()
        self.assertLess(old, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        base_dict = self.base.to_dict()
        self.assertEqual(dict, type(base_dict))
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(),
                         base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(),
                         base_dict["updated_at"])
        self.assertEqual(base_dict.get("_sa_instance_state", None), None)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_delete(self):
        """Test delete method."""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
=======
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        dictionary = {}
        dictionary.update(i.__dict__)
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         dictionary))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
