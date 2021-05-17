#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    token = 0
    try:
        for token in range(x):
            print(my_list[token], end='')
    except IndexError:
        pass
    print()
    return (token)
