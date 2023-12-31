#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defining common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            args: Unused
            kwargs: Dictionary of attributes
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            String representation of the object.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
            Dictionary representation of the object.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Creates a new instance from a dictionary representation.

        Args:
            obj_dict: Dictionary representation of the object.

        Returns:
            New instance of the class.
        """
        return cls(**obj_dict)

# Uncomment the following lines if you want to test this module separately
# if __name__ == '__main__':
#     my_model = BaseModel()
#     my_model.name = "My_First_Model"
#     my_model.my_number = 89
#     print(my_model.id)
#     print(my_model)
#     print(type(my_model.created_at))
#     print("--")
#     my_model_json = my_model.to_dict()
#     print(my_model_json)
#     print("JSON of my_model:")
#     for key in my_model_json.keys():
#          print("\t{}: ({}) - {}".format
#               (key, type(my_model_json[key]), my_model_json[key]))
#
#     print("--")
#     my_new_model = BaseModel.from_dict(my_model_json)
#     print(my_new_model.id)
#     print(my_new_model)
#     print(type(my_new_model.created_at))
#
#     print("--")
#     print(my_model is my_new_model)
