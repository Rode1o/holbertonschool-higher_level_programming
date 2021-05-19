#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 5-square.py)

"""


class Square:
    """Write a class that definesa square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) \
           or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size != 0:
            for token in range(self.size):
                print('_' * self.position[0], end="")
                print('#' * self.size)
        else:
            print()