#!/usr/bin/python3
"""Unittests for User class"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_attributes(self):
        """Test User class attributes"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_str_method(self):
        """Test __str__ method"""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        user = User()
        expected_dict = {
            'id': user.id,
            '__class__': 'User',
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            'email': user.email,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_save_method(self):
        """Test save method"""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

