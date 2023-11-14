#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime

class BaseModelTests(unittest.TestCase):
    """
        testing the base model
    """

    my_mod = BaseModel()

    def testBaseModel1(self):
        """
            Testing attribute values
        """
        self.my_mod.name = "Hamed"
        self.my_mod.my_number = 99
        self.my_mod.save()
        my_mod_json = self.my_mod.to_dict()

        self.assertEqual(self.my_mod.name, my_mo_json['name'])
        self.assertEqual(self.my_mod.my_number, my_mod_json['my_number'])
        self.assertEqual('BaseModel', my_mod_json['__class__'])
        self.assertEqual(self.my_mod.id, my_mod_json['id'])

    def testSave(self):
        """
            Testing the saving method
        """
        self.my_mod.first_name = "Chadha"
        self.my_mod.save()

        self.assertIsInstance(self.my_mod.id, str)
        self.assertIsInstance(self.my_mod.created_at, datetime.datetime)
        self.assertIsInstance(self.my_mod.updated_at, datetime.datetime)

        first_dic = self.my_mod.to_dict()

        self.my_mod.first_name = "HAMED"
        self.my_mod.save()
        sec_dic = self.my_mod.to_dict()

        self.assertEqual(first_dic['created_at'], sec_dic['created_at'])
        self.assertNotEqual(first_dic['updated_at'], sec_dic['updated_at'])

if __name__ == '__main__':
    unittest.main()
