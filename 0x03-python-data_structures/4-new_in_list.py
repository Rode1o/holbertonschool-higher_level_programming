#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _list = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    _list[idx] = element
    return _list
