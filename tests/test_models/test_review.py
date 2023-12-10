#!/usr/bin/python3
"""Unittests for Review class"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test Review class attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

