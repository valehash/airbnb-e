#!/usr/bin/python3

import uuid 
from . import storage as mp
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        fmt_str = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs['__class__']
            for k,v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, fmt_str)
                setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            mp.new(self)

    def __str__(self): 
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        mp.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] =  self.__class__.__name__
        new_dict['updated_at'] =  new_dict['updated_at'].isoformat()
        new_dict['created_at'] =  new_dict['created_at'].isoformat()
        return new_dict

