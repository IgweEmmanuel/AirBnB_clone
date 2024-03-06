#!/usr/bin/python3

a = {"name" : "ken", "age" : 12}

def fun(name,age):
    print(name,age)
fun(**a)
