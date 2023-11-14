#!/usr/bin/python3
"""
Unittest for user
"""
import unittest
from models.user import User
import datetime

class UserCase(unittest.TestCase):
    """
        Tests the user class
    """

    us = User()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.us)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.us, User)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.us, 'email'))
        self.assertTrue(hasattr(self.us, 'password'))
        self.assertTrue(hasattr(self.us, 'first_name'))
        self.assertTrue(hasattr(self.us, 'last_name'))
        self.assertTrue(hasattr(self.us, 'id'))
        self.assertTrue(hasattr(self.us, 'created_at'))
        self.assertTrue(hasattr(self.us, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.us.first_name, str)
        self.assertIsInstance(self.us.last_name, str)
        self.assertIsInstance(self.us.email, str)
        self.assertIsInstance(self.us.password, str)
        self.assertIsInstance(self.us.id, str)
        self.assertIsInstance(self.us.created_at, datetime.datetime)
        self.assertIsInstance(self.us.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
