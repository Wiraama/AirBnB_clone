import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    """ testing class """

    def setUp(self):
        """sets uo the test environment """
        self.model =BaseModel()

    def test_id_uuid(self):
        """ tests if id is valid UUID"""
        self.assertIsInstance(self.model.id, str)
        try:
            uuid.obj = uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("not valid UUID")
        self.assertEqual(str(uuid.obj), self.model.id)

    def test_created_at_is_datetime(self):
        """tesr created at"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """ test if the updated at is a adtetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """testing str method"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """testing the save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_to_dict(self):
        """testing for dict"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

if __name__ == '__main__':
    unittest.main()
