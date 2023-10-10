#!/usr/bin/env python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBase_instantiation(unittest.TestCase):

	def test_uuid(self):
		"""Test that id is correctly created"""
		model = BaseModel()
		model2 = BaseModel()
		self.assertTrue(hasattr(model2, "id"))
		self.assertEqual(type(model.id), str)
		self.assertNotEqual(model.id, model2.id)

	def test_created_at(self):
		"""Test that created_at is correctly created"""
		model = BaseModel()
		model2 = BaseModel()
		self.assertEqual(type(model.created_at), datetime)
		self.assertNotEqual(model.created_at, model2.created_at)

	def test_updated_at(self):
		"""Test that updated_at is correctly created"""
		model = BaseModel()
		model2 = BaseModel()
		self.assertEqual(type(model.updated_at), datetime)
		self.assertNotEqual(model.updated_at, model2.updated_at)

	def test_str(self):
		"""Test that the str method has the correct output"""
		model = BaseModel()
		string = "[{}] ({}) {}".format(model.__class__.__name__, model.id, model.__dict__)
		self.assertEqual(string, str(model))

	def test_save(self):
		"""Test that save updates the attribute updated_at"""
		model = BaseModel()
		updated = model.updated_at
		model.save()
		self.assertNotEqual(updated, model.updated_at)

	def test_to_dict(self):
		"""Test that to_dict returns the correct dictionary"""
		model = BaseModel()
		model_dict = model.to_dict()
		self.assertEqual(type(model_dict), dict)
		self.assertEqual(model_dict['__class__'], 'BaseModel')
		self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
		self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
		self.assertEqual(type(model_dict['id']), str)