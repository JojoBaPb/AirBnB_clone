#!/usr/bin/python3
"""
Module for BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class for all common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
    """
    Initialize BaseModel class
    """

    from models import storage
    if not kwargs:
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        storage.new(self)
    else:
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
    """
    Prints string rep of BaseModel object.
    [<class name>] (<self.id>) <self.__dict__>
    """
    return "[{}] ({}) {}".format(type(self).__name__, self.id,self.__dict__)

    def save(self):
    """
    Updates 'updated_at' with the current datetime
    """
    from models import storage
    self.updated_at = datetime.now()
    storage.save()

    def to_dict(self):
    """
    Returns dictionary containing all keys/values of __dict__
    of the instance:

    * ONLY instance attributes set will be returned
    * a key __class__ added with class name of object
    * 'created_at' and 'updated_at' to be converted to string object in ISO
    format
    """
    dict1 = self.__dict__.copy()
    dict1['__class__'] = self.__class__.__name__
    dict1['created_at'] = self.created_at.isoformat()
    dict1['updated_at'] = self.updated_at.isoformat()
    return dict1
