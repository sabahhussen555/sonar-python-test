# app.py
import os

def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # Bug: no check for division by zero

def get_password():
    password = "admin123"  # Vulnerability: hardcoded password
    return password

def unused_function():
    x = 10  # Code smell: unused variable
    pass

def duplicate_block():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")  # Code smell: duplication
