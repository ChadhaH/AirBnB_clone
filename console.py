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

    def do_create(self, commands):
        """
            Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id
        """

        command = parse(commands)
        if command == "" or command is None:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        print(eval(command[0])().id)
        storage.save()

    def do_show(self, args):
        """
            Prints the string representation of an instance based on the class name and id
        """

        arg = parse(args)
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
        """

        arg = parse(args)
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, commands):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        command = parse(commands)
        if command[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            instances = []
            for k, v in objs.items():
                obj_name = value.__class__.__name__
                if obj_name == command[0]:
                    instances += [value.__str__()]
            print(instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
