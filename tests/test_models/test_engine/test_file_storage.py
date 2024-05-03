#!/usr/bin/python3
"""
test module for testing file_storage
"""

import unittest
import inspect
import pycodestyle
import json
import os
from os import getenv
from models.base_model import BaseModel
from models.engine import file_storage
from models.state import State
FileStorage = file_storage.FileStorage


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
                 "system setup to use DB storage")
class TestFileStorage(unittest.TestCase):
    """ Test for FileStorage class """

    def setUp(self):
        """ general test setup, will create a temp baseModel """
        self.storage = FileStorage()
        self.full_dict = self.storage.all()
        self.save = FileStorage._FileStorage__objects

    def tearDown(self):
        """ general tear down, will delete the temp baseModel """
        self.temp_b = None
        self.full_dict = None
        FileStorage._FileStorage__objects = self.save

    def test_all_returns_type(self):
        """Test that all returns the correct file"""
        self.assertEqual(type(self.full_dict), dict)
        self.assertIs(self.full_dict, self.storage._FileStorage__objects)

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        os.remove("file.json")
        new_dict = {}
        instance = BaseModel()
        instance_key = instance.__class__.__name__ + "." + instance.id
        new_dict[instance_key] = instance
        FileStorage._FileStorage__objects = new_dict
        self.storage.save()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        instance = BaseModel()
        instance_key = instance.__class__.__name__ + "." + instance.id
        self.storage.new(instance)
        test_dict[instance_key] = instance
        self.assertEqual(test_dict, self.storage._FileStorage__objects)

    def test_get_fs(self):
        """Testing the file get fs method"""
        fs_obj = FileStorage()
        state = State()
        # add the new state to the file_storage
        fs_obj.new(state)
        first_state_id = list(self.storage.all("State").values())[0].id
        self.assertEqual(type(self.storage.get("State", first_state_id)), State)

    def test_count_fs(self):
        """Testing the file_storage count method"""
        self.storage.reload()
        res = self.storage.all(None)
        cn = self.storage.count(None)
        self.assertEqual(len(res), cn)
        res1 = self.storage.all("State")
        cn1 = self.storage.count("State")
        self.assertEqual(len(res1), cn1)
