#!/usr/bin/python3
"""Python class MagicClass that
does exactly the same as a give Python bytecode"""
import math


class MagicClass:
    """Python class """
    def __init__(self, radius=0):
        self.radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius
        
    def area(self):
        return (self.radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi) * self.__radius
