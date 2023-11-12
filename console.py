#!/usr/bin/python3
"""
    Represents the HBnB console
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
        Represents the HBnB custom prompt

        prompt (str): The command prompt
    """
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, command):
        """
            a command to quit the console
        """
        return True

    def do_EOF(self, line):
        """
            a line that exists when receiving EOF
        """
        print("")
        return True
    
    def emptyline(self):
        """
            nothing happens when receiving an empty line
        """
        pass

    def do_create(self, command):
        """
            Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id
        """
        if command == "" or command is None:
            print("** class name missing **")
        elif command not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        print(eval(command[0])().id)
        storage.save()


