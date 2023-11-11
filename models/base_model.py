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


