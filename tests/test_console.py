import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.base_model = BaseModel()
        self.user = User()

    def tearDown(self):
        self.console.do_destroy("BaseModel {}".format(self.base_model.id))
        self.console.do_destroy("User {}".format(self.user.id))

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
        self.assertIn("BaseModel.{}".format(base_model_id), output)
        self.assertIn("User.{}".format(user_id), output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(base_model_id))
            base_model_output = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(user_id))
            user_output = f.getvalue().strip()
        self.assertIn(base_model_id, base_model_output)
        self.assertIn(user_id, user_output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertIn("BaseModel.{}".format(
            base_model_id), self.console.do_all(""))
        self.assertIn("User.{}".format(user_id), self.console.do_all(""))
        self.console.onecmd("destroy BaseModel {}".format(base_model_id))
        self.console.onecmd("destroy User {}".format(user_id))
        self.assertNotIn("BaseModel.{}".format(
            base_model_id), self.console.do_all(""))
        self.assertNotIn("User.{}".format(user_id), self.console.do_all(""))

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertNotIn("first_name", self.console.do_show(
            "BaseModel {}".format(base_model_id)))
        self.assertNotIn("email", self.console.do_show(
            "User {}".format(user_id)))
        self.console.onecmd(
            'update BaseModel {} first_name "John"'.format(base_model_id))
        self.console.onecmd(
            'update User {} email "john@example.com"'.format(user_id))
        self.assertIn("first_name", self.console.do_show(
            "BaseModel {}".format(base_model_id)))
        self.assertIn("email", self.console.do_show("User {}".format(user_id)))

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            base_model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertIn("BaseModel.{}".format(
            base_model_id), self.console.do_all(""))
        self.assertIn("User.{}".format(user_id), self.console.do_all(""))
