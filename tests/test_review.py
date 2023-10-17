#!/usr/bin/env python3
"""Defines the Review class."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """test the Review class"""

    def test_attributes(self):
        """test the attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        """test setting the attributes"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place to stay!")

    def test_type(self):
        """test the type of the Review attribute"""
        review = Review()
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)

if __name__ == "__main__":
    unittest.main()
