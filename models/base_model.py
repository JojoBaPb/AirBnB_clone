#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            # Update attributes based on kwargs dictionary
                                                kwargs.pop('__class__', None)  # Remove '__class__' key if present
                                                            for key, value in kwargs.items():
                                                                if key in ('created_at', 'updated_at'):
                                                                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                        setattr(self, key, value)
                                                                                                                    else:
                                                                                                                        # Create new instance with id and created_at
                                                                                                                                                            self.id = str(uuid.uuid4())
                                                                                                                                                                        self.created_at = datetime.now()
                                                                                                                                                                                    self.updated_at = datetime.now()

                                                                                                                                                                                        def __str__(self):
                                                                                                                                                                                            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

                                                                                                                                                                                        def save(self):
                                                                                                                                                                                            self.updated_at = datetime.now()

                                                                                                                                                                                                                    def to_dict(self):
                                                                                                                                                                                                                        data = self.__dict__.copy()
                                                                                                                                                                                                                                        data['__class__'] = self.__class__.__name__
                                                                                                                                                                                                                                                data['created_at'] = self.created_at.isoformat()
                                                                                                                                                                                                                                                        data['updated_at'] = self.updated_at.isoformat()
                                                                                                                                                                                                                                                                return data

