#!/usr/bin/env python3

"""Defines the City class."""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """test the City class"""

    def test_state_id(self):
        """test the state_id attribute"""
        city = City()
        self.assertEqual(city.state_id, "")
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name(self):
        """test the name attribute"""
        city = City()
        self.assertEqual(city.name, "")
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_type(self):
        """test the type of the City attribute"""
        city = City()
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)

if __name__ == "__main__":
    unittest.main()
