#!/usr/bin/env python3
"""Tests the User class."""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """test the User class"""

    def test_attributes(self):
        """test the attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_attributes(self):
        """test setting the attributes"""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_type(self):
        """test the type of the User attribute"""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

if __name__ == "__main__":
    unittest.main()
