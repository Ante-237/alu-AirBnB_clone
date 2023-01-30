#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage


class TestCaseFileStorageEngine(unittest.TestCase):

    def setUp(self):
        """ setup for various test to be done
        and creating the various objects """
        self.all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in self.all_objs.keys():
            obj = self.all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model.save()
        print(self.my_model)
        # self.assertEqual(self.my_model.name, "My_First_Model")

    def test_Number(self):
        """ checking if reloaded model
        has the same class as previously """
        self.assertEqual(self.my_model.__class__.__name__, "BaseModel")

    def test_NameOfModel(self):
        """ test if name reflex previous name"""
        self.assertEqual(self.my_model.name, "My_First_Model")

    def test_ClassName(self):
        """ checking the class name sure """
        self.assertEqual(self.my_model.to_dict()['my_number'], 89)



