#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for letter in str:
        if i != n:
            print("{}".format(letter), end="")
        i = i+1
    return ""