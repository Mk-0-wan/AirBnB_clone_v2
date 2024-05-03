#!/usr/bin/python3
"""
test module for testing file_storage
"""

import unittest
import inspect
import pycodestyle
import models
import MySQLdb
import console
from unittest.mock import patch
from io import StringIO
from os import getenv
from models.engine import db_storage
DBStorage = db_storage.DBStorage
HBNBCommand = console.HBNBCommand


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(DBStorage.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(DBStorage.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                 "system setup to use file_storage")
class TestDBStorage(unittest.TestCase):
    """ Test for DBstorage class """
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    def test_create_state_works(self):
        """tests create state"""
        self.consol = HBNBCommand()
        SQLdbConnection = MySQLdb.connect(host="localhost",
                                          port=3306,
                                          user="hbnb_test",
                                          passwd="hbnb_test",
                                          db="hbnb_test_db")
        dbCurser = SQLdbConnection.cursor()
        dbCurser.execute('''
                        SELECT * FROM users
                        ''')
        LenBeforeCreate = len(dbCurser.fetchall())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User')
            dbCurser.execute('''
                        SELECT * FROM users
                        ''')
            lenAfterCreate = len(dbCurser.fetchall())
            self.assertEqual((LenBeforeCreate + 1), lenAfterCreate)
        dbCurser.close()
        SQLdbConnection.close()
        del self.consol
