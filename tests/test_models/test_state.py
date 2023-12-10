#!/usr/bin/python3
"""Unittests for State class"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test State class attributes"""
        state = State()
        self.assertEqual(state.name, "")

