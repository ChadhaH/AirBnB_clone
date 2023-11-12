#!/usr/bin/python3

"""
    Script for the BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializing new instance attributes

        Arguments:
            - *args: list of arguments
            - **kwargs: dict of key-values
        """

        dateform = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:

                    self.__dict__[k] = kwargs[k]

    def __str__(self):
        """
            Returns a string representation of the base model class
        """
        classN = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(classN, self.id, self.__dict__)

    def save(self):
        """
             updates the public instance attribute updated_at
             with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['__class__'] = self.__class__.__name__

        return (dic)
