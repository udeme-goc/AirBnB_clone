#!/usr/bin/python3
"""Unittests for BaseModel class"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_attributes(self):
        """Test BaseModel class attributes"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_str_method(self):
        """Test __str__ method"""
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        base_model = BaseModel()
        expected_dict = {
            'id': base_model.id,
            '__class__': 'BaseModel',
            'created_at': base_model.created_at.isoformat(),
            'updated_at': base_model.updated_at.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), expected_dict)

    def test_save_method(self):
        """Test save method"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(old_updated_at, base_model.updated_at)

