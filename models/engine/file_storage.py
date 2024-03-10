#!/usr/bin/python3
from os import path
import json
from singleton import my_classes

class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ser = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as js:
            # print("saving............................")
            js.write(json.dumps(ser))

    def reload(self):
        if not path.exists(self.__file_path):
            return
        with open(self.__file_path) as js:
            
            dic = json.loads(js.read())
            dt = {}
            for key, value in dic.items():
                dt |= {key: my_classes[key.split(".")[0]](**value)}
