#!/usr/bin/python3
""" class BaseGeometry (based on 6-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class BaseGeometry (based on 6-base_geometry.py"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.heigth = height
