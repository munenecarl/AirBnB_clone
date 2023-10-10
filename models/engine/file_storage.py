#!/usr/bin/env python3
"""Defines the FileStorage class."""

import json
import os

from models.base_model import BaseModel


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                dict = json.load(file)
                for key, value in dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj
