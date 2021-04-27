#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastnumber = ((number * - 1) % 10) * -1
else:
    lastnumber = number % 10
if lastnumber > 5:
    print('Last digit of {0} is {1}'
          ' and is greater than 5'.format(number, lastnumber))
elif lastnumber == 0:
    print('Last digit of {0} is {1}'
          ' and is 0'.format(number, lastnumber))
else:
    print('Last digit of {0} is {1}'
          ' and is less than 6 and not 0'.format(number, lastnumber))
