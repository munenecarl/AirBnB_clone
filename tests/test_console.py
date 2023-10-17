#!/usr/bin/env python3

import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_emptyline(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_create(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_destroy(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_all(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_count(self):
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertEqual("0\n", f.getvalue())

if __name__ == '__main__':
    unittest.main()