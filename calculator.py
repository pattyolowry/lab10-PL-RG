# https://github.com/pattyolowry/lab10-PL-RG
# Partner 1: Patrick Lowry
# Partner 2: Ria Gupta
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # b / a  (yes — the assignment wants it in this order)
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero: a is 0.")
    return b / a

def log(a, b):
    # log_a(b)
    if a <= 0 or a == 1:
        raise ValueError("Base 'a' must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument 'b' must be positive.")
    return math.log(b, a)

def exp(a, b):
    # a^b
    return a ** b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a == 0 or b == 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b