# https://github.com/pattyolowry/lab10-PL-RG
# Partner 1: Patrick Lowry
# Partner 2: Ria Gupta
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    # b / a  (yes — the assignment wants it in this order)
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero: a is 0.")
    return b / a

def exp(a, b):
    # a^b
    return a ** b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a < 0 or b < 0 or b == 1:
        raise ValueError
    return math.log(b, a)