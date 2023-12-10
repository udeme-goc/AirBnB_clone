#!/usr/bin/python3
"""Unittests for Amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attributes(self):
        """Test Amenity class attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

