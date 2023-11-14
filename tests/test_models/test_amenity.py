#!/usr/bin/python3
"""
    Defines unittests for models/amenity.py.
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        am_1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am_1.__dict__)

    def test_two_amenities_unique_ids(self):
        am_2 = Amenity()
        am_3 = Amenity()
        self.assertNotEqual(am_2.id, am_3.id)

    def test_two_amenities_different_created_at(self):
        am2 = Amenity()
        sleep(0.05)
        am3 = Amenity()
        self.assertLess(am2.created_at, am3.created_at)

    def test_two_amenities_different_updated_at(self):
        am2 = Amenity()
        sleep(0.05)
        am3 = Amenity()
        self.assertLess(am2.updated_at, am3.updated_at)

    def test_str_representation(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        am1 = Amenity()
        am1.id = "123456"
        am1.created_at = am1.updated_at = dat
        am1str = am1.__str__()
        self.assertIn("[Amenity] (123456)", am1str)
        self.assertIn("'id': '123456'", am1str)
        self.assertIn("'created_at': " + dat_repr, am1str)
        self.assertIn("'updated_at': " + dat_repr, am1str)

    def test_args_unused(self):
        am1 = Amenity(None)
        self.assertNotIn(None, am1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dat = datetime.today()
        dat_iso = dat.isoformat()
        am1 = Amenity(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(am1.id, "345")
        self.assertEqual(am1.created_at, dat)
        self.assertEqual(am1.updated_at, dat)
        
    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """
        Testing saving methon
    """
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am1 = Amenity()
        sleep(0.05)
        first_updated_at = am1.updated_at
        am1.save()
        self.assertLess(first_updated_at, am1.updated_at)

    def test_two_saves(self):
        am1 = Amenity()
        sleep(0.05)
        first_updated_at = am1.updated_at
        am1.save()
        second_updated_at = am1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am1.save()
        self.assertLess(second_updated_at, am1.updated_at)

    def test_save_with_arg(self):
        am1 = Amenity()
        with self.assertRaises(TypeError):
            am1.save(None)

    def test_save_updates_file(self):
        am1 = Amenity()
        am1.save()
        am1id = "Amenity." + am1.id
        with open("file.json", "r") as fc:
            self.assertIn(am1id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
        testing to_dict methond
    """
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

     def test_to_dict_contains_correct_keys(self):
        am1 = Amenity()
        self.assertIn("id", am1.to_dict())
        self.assertIn("created_at", am1.to_dict())
        self.assertIn("updated_at", am1.to_dict())
        self.assertIn("__class__", am1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am1 = Amenity()
        am1.middle_name = "Hamed"
        am1.my_number = 99
        self.assertEqual("Hamed", am1.middle_name)
        self.assertIn("my_number", am1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am1 = Amenity()
        am1_dict = am1.to_dict()
        self.assertEqual(str, type(am1_dict["id"]))
        self.assertEqual(str, type(am1_dict["created_at"]))
        self.assertEqual(str, type(am1_dict["updated_at"]))

    def test_to_dict_output(self):
        dat = datetime.today()
        am1 = Amenity()
        am1.id = "123456"
        am1.created_at = am1.updated_at = dat
        tidict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat(),
        }
        self.assertDictEqual(am1.to_dict(), tidict)

    def test_contrast_to_dict_dunder_dict(self):
        am1 = Amenity()
        self.assertNotEqual(am1.to_dict(), am1.__dict__)

    def test_to_dict_with_arg(self):
        am1 = Amenity()
        with self.assertRaises(TypeError):
            am1.to_dict(None)

if __name__ == "__main__":
    unittest.main()
