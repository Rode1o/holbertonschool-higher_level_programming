#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _list = []
    for token in range(list_length):
        try:
            _list.append(my_list_1[token] / my_list_2[token])
        except ZeroDivisionError:
            _list.append(0)
            print("division by 0")
        except TypeError:
            _list.append(0)
            print("wrong type")
        except IndexError:
            _list.append(0)
            print("out of range")
        finally:
            pass
    return _list
