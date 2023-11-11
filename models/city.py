#!/usr/bin/python3
"""
    This model defines the User city
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Represent the city class:

        state_id (str): id for the state.
        name (str): The city name.

    """
    state_id = ""
    name = ""
