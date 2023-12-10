#!/usr/bin/python3
"""Unittests for City class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test City class attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

