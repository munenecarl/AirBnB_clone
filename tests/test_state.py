#!/usr/bin/env python3
"""Defines the State class."""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """test the State class"""

    def test_name(self):
        """test the name attribute"""
        state = State()
        self.assertEqual(state.name, "")
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_inheritance(self):
        """test that State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_type(self):
        """test the type of the State attribute"""
        state = State()
        self.assertEqual(type(state.name), str)

if __name__ == "__main__":
    unittest.main()
