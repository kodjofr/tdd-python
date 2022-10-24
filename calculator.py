"""
just some functions to test
"""

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError("can not divide by zero")
    return x/y

def square(x):
    return x*x

def square_root(x):
    return x**0.5

