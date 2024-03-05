#!/usr/bin/python3
"""
A BaseModel class that defines all common attributes/methods for other classes
"""


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    import uuid
    from datetime import datetime


    def __init__(self):
    """
    This is where all the attributes will be defined
    """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
    """
    prints the string representation of the instance object
    """
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    
