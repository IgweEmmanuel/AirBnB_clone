#!/usr/bin/python3
a = {"name" : "Ken", "age": 12, "gender" : "non"}
class Test:
    def __init__(self, *args, **kwargs):
        print(*kwargs.values())
Test(**a)

