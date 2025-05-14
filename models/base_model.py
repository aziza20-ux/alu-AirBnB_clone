#!/usr/bin/python3

import uuid
form datetime import datetime

class BaseModel:
    """the constructor of the class '__init__'"""
    def __init__(self, *args, **kwargvs):
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """it will return the string represation of object"""

        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """this method will save the last time object was modified"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """the method to returm dictionary of the attributes of any object"""
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        
        return obj_dict
