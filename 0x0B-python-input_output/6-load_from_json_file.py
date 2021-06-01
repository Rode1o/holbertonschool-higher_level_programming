#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
