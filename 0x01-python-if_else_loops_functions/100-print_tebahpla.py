#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        lower = chr(letter)
    else:
        lower = chr(letter - 32)
    print("{}".format(lower), end="")
