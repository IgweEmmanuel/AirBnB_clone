#!/usr/bin/python3
from os import path
import json

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
            js.write(json.dumps(ser))

    def reload(self):
        if not path.exists(self.__file_path):
            return
        with open(self.__file_path) as js:
            dic = json.load(js)
            for key, value in dic.items():
                cls_name, ins_id = key.split('.')
                clas = eval(cls_name)
                ins = clas(**value)
                self.new(ins)


