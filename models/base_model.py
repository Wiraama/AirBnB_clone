#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """ this class should define all attributes/methods for other classes """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
    

    def to_dict(self):
        """ dictionary from instances """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__

        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep


    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
