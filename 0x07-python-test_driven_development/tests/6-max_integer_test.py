#!/usr/bin/python3
"""Unittest for max_integer([xxxxxxx])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """Unit test class"""
    def test_alone(self):
        item = [9]
        self.assertEqual(max_integer(item), 9)

    def test_empty(self):
        item = []
        self.assertEqual(max_integer(item), None)

    def test_two_max_numbers(self):
        item = [1, 2, 3, 5, 7, 9, 6, 9]
        self.assertEqual(max_integer(item), 9)

    def test_strings(self):
        item = "Yoshi"
        self.assertEqual(max_integer(item), 's')

    def test_remix(self):
        item = ['T', 7, 3.0]
        with self.assertRaises(TypeError):
            max_integer(item)

    def test_negative(self):
        item = [-23, -48, -13, -9]
        self.assertEqual(max_integer(item), -9)

    def test_floats(self):
        item = [1.0, 2.7, 5.8, 4.0]
        self.assertEqual(max_integer(item), 5.8)

    def test_maxbegining(self):
        item = [7, 4, 6, 3]
        self.assertEqual(max_integer(item), 7)

if __name__ == '__main__':
    unittest.main()
