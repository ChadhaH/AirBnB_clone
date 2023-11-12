#!/usr/bin/python3
"""
    This model defines the User place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the place class:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The place name.
        description (str): The place description.
        number_rooms (int): Number of rooms available.
        number_bathrooms (int): Number of bathrooms available.
        max_guest (int): Maximum number of guests.
        price_by_night (int): Price by night.
        latitude (float): The place latitude.
        longitude (float): The place longitude.
        amenity_ids (list): list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
