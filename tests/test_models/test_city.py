#!/usr/bin/python3
"""
Unittest for user
"""
import unittest
from models.city import City
import datetime

class TestCity(unittest.TestCase):
    """
        Testing the city class
    """

    ci = City()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.ci)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.ci, City)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.c,i 'state_id'))
        self.assertTrue(hasattr(self.ci, 'name'))
        self.assertTrue(hasattr(self.ci, 'id'))
        self.assertTrue(hasattr(self.ci, 'created_at'))
        self.assertTrue(hasattr(self.ci, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.ci.state_id, str)
        self.assertIsInstance(self.ci.name, str)
        self.assertIsInstance(self.ci.id, str)
        self.assertIsInstance(self.ci.created_at, datetime.datetime)
        self.assertIsInstance(self.ci.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
