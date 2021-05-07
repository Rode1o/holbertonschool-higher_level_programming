#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _list = my_list.copy()
    for token in range(len(_list)):
        if _list[token] == search:
            _list[token] = replace
    return[_list]
