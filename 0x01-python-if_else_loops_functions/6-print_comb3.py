#!/usr/bin/python3
for zero_to in range(0, 100):
    a = zero_to % 10
    b = zero_to / 10
    if b < a and zero_to != 89:
        print("{:02}, ".format(zero_to), end="")
    elif zero_to == 89:
        print("{}".format(zero_to))