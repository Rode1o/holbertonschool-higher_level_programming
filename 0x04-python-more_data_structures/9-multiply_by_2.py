#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _dictionary = a_dictionary.copy()
    for token in a_dictionary:
        _dictionary[token] = _dictionary[token] * 2
    return _dictionary
