#!/usr/bin/python3
"""Module to test BaseModel class"""


from datetime import datetime
import unittest
import io
from models.base_model import BaseModel
from contextlib import redirect_stdout

class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    # -------------Tests Public Attributes--------------------------------------

    def test_idCorrect(self):
        """Test that id is a unique string"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertTrue((type(my_model1.id) is str))
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_createUpdateType(self):
        """Test that create and update are datetime objects"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))

    def test_updateDif(self):
        """Test that update is different than create after update"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_strCorrect(self):
        """Test that str works correctly"""
        my_model = BaseModel()
        f = io.StringIO()
        s = "[BaseModel] ({}) {}\n".format(my_model.id, my_model.__dict__)
        with redirect_stdout(f):
            print(my_model)
        self.assertEqual(f.getvalue(), s)