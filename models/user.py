#!/usr/bin/python3
"""
    Represents the User class
"""

class User(BaseModel):
    """
         the user and it inherits from BaseModel

        email (str): The user email.
        password (str): The user password.
        first_name (str): The user first name.
        last_name (str): The user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
