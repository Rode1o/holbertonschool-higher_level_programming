#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for token in sorted(a_dictionary.keys()):
        print("{}: {}".format(token, a_dictionary[token]))
