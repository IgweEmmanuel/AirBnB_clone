#!/usr/bin/python3
"""
A BaseModel class that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    import uuid
    from datetime import datetime
    

    def __init__(self, **kwargs):
        """
        This is where all the attributes will be defined
        """
        if kwargs:
            self.id = kwargs.get("id")
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        prints the string representation of the instance object
        """
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the public updated_at attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return {
                "created_at": self.created_at.isoformat()
                "updated_at": self.updated_at.isoformat()
                "__class__": self.__class__.__name__
                "id": self.id
        }

catt = BaseModel.to_dict() 
BaseModel(**catt)
 
