#!/usr/bin/env python3

"""Tests the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """test the Amenity class"""

    def test_name(self):
        """test the name attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_inheritance(self):
        """test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_type(self):
        """test the type of the Amenity attribute"""
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

if __name__ == "__main__":
    unittest.main()
