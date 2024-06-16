#!usr/bin/python3
""" module to create a class baseclass defining common attributes """

import uuid
from datetime import datetime

class BaseModel:
    """ the class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """copying"""
        dict_rep = self.__dict__.copy()
        """adding class key"""
        dict_rep['__class__'] = self.__class__.__name__
        """converting to ISO format string"""
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep
