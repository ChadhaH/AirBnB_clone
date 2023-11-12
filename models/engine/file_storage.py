#!/usr/bin/python3
"""
    Represents the File Storage class
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json
import os


class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances

        __file_path (str): where to save the objects
        __objects (dict): the objects to be saved
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns all the objects saved
        """

        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key
        """
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """

        obdic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fc:
            json.dump(obdic, fc)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as fc:
                obdic = json.load(fc)
            for k in obdic.values():
                cname = o["__class__"]
                del o["__class__"]
                self.new(eval(cname)(**o))
        except FileNotFoundError:
            return
