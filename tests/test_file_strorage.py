import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = storage
        self.base_model = BaseModel()
        self.user = User()

    def tearDown(self):
        self.storage.reload()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)
        self.assertIsInstance(self.storage.all(BaseModel), dict)
        self.assertIsInstance(self.storage.all(User), dict)

    def test_new(self):
        self.storage.new(self.base_model)
        self.assertIn("BaseModel.{}".format(
            self.base_model.id), self.storage.all())
        self.storage.new(self.user)
        self.assertIn("User.{}".format(self.user.id), self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            data = f.read()
            self.assertIn("BaseModel.{}".format(self.base_model.id), data)
            self.assertIn("User.{}".format(self.user.id), data)

    def test_reload(self):
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(
            self.base_model.id), self.storage.all())
        self.assertIn("User.{}".format(self.user.id), self.storage.all())
