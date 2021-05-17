#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    token_elements = 0
    for _elements in range(x):
        try:
            print("{:d}".format(my_list[_elements]), end='')
            token_elements += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return (token_elements)
