#!/usr/bin/python3
a = {"name" : "Ken", "age": 12, "gender" : "non"}
class Test:
    def __init__(self, name, age=None, gender=None):
        print(name, age, gender)
Test(**a)

