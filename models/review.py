#!/usr/bin/python3
"""
    This model represents the User review
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represent the review class:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review.
    """

    place_id = ""
    user_id = ""
    text = ""
