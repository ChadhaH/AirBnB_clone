#!/usr/bin/python3
"""
    This model defines the User state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent the state class:

        name (str): The state name.

    """
    name = ""
