#!/usr/bin/python3
"""
    This model defines the User amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent the amenity class:

        name (str): The amenity name.

    """
    name = ""
