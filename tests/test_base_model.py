#!/usr/bin/python3
import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ test for each function """


    def setUp(self):
        self.model = BaseModel()


    def test_instance_creation(self):
        """ cheakin if its correctly initiated """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """ tests if safe method update or not """
        old = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old)

    def test_to_dict_method(self):
        """ test to check if returned is dictionary with correct keys """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str_method(self):
        """ test if correct string is returned from __str__ """
        expect_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expect_str)


if __name__ == '__main__':
    unittest.main()
