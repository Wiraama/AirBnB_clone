#!/usr/bin/python3
import unittest
from datetime import datetime
from models.tmp_base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_instance_creation(self):
        """Test if an instance of BaseModel is created properly"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        model = BaseModel()
        model_str = model.__str__()
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(f"({model.id})", model_str)

    def test_save_method(self):
        """Test the save method updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_method(self):
        """Test to_dict method creates a dictionary with correct keys"""
        model = BaseModel()
        model_dict = model.to_dict()
        
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

        # Check if created_at and updated_at are ISO format strings
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

