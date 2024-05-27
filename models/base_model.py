""" model/basemodel.py"""
import uuid
from datetime import datetime

""" BASECLASS"""
class BaseModel:
    """ Base class for other models """

    def __init__(self):
        """ initiates a new basemodel instance """
        self.id = str.(uuid.uuid4())
        self.time_create = datetime.now()
        self.update_at = self.time_create

    def __str__(self):
        """ returns string representation if instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def saving(self):
        """ update the public insatnce to current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary containing all keywords and values of dict"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['time_create'] = self.time_create.isoformat()
        result['update_at'] = self.update_at.isoformat()

        return result
