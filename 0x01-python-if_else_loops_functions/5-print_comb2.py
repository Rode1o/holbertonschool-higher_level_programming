#!/usr/bin/python3
for zero_to in range(0, 100):
    if zero_to == 99:
        print("{}".format(zero_to))
    else:
        print("{:02}, ".format(zero_to), end="")
