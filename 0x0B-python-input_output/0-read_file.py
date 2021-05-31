#!/usr/bin/python3
"""holberton care berga"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, mode='r', encoding='utf-8') as my_file:
        print(my_file.read(), end="")
