""" model/basemodel.py"""
import uuid
from datetime import datetime

""" BASECLASS"""


class BaseModel:
    """ Base class for other models """

    def __init__(self):
        """ initiates a new basemodel instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns string representation if instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the public insatnce to current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary containing all keywords and values of dict"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result
