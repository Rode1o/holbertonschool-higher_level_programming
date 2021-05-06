#!/usr/bin/python3
def max_integer(my_list=[]):
    big = len(my_list)
    my_list.sort()
    if big != 0:
        return my_list[-1]
    else:
        return None
