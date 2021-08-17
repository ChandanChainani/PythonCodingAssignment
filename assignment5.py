from random import random
from math import floor
import re
import sys

MAX_LIFTS = 5
MAX_FLOORS = 20

digit_word_regex = re.compile('([0-9]+)([UD])?', re.IGNORECASE)
directions = ['', 'U', 'D']

lifts = {}
while len(lifts) < MAX_LIFTS:
    r = str(floor(random() * (MAX_FLOORS - 1) + 1)) + directions[floor(random() * 3)]
    lifts[r] = r
lifts = list(lifts.keys())
print("> lift_position = ", lifts)

user_request = digit_word_regex.search(input("> Enter a request? "))
user_pos = int(user_request.group(1))
user_dir = user_request.group(2)
if user_request.group(1) != None and user_request.group(2) != None:
    index, _min = 0, int(digit_word_regex.search(lifts[0]).group(1)) - user_pos
    for i in range(1, len(lifts)):
        founds = digit_word_regex.search(lifts[i])
        if founds:
            position = int(founds.group(1))
            direction = founds.group(2)
            difference = position - user_pos
            if direction == user_dir or direction == None:
                print(user_dir, direction, _min, position, user_pos, difference)
                if direction == 'D' and difference < _min and position > user_pos:
                    _min, index = difference, i
                elif direction == 'U' and difference < _min and position < user_pos:
                    _min, index = difference, i
            # elif direction == None:
            #     if user_dir == 'D' and position > user_pos:
            #         _min, index = difference, i
            #     elif user_dir == 'U' and position < user_pos:
            #         _min, index = difference, i
            # if (direction == user_pos):
            #     print('same direction')

            # if (direction == None):
            #     print("none")
            # if _min == None or (_min > difference and (direction == None or direction == user_request.group(2))):
            #     _min, index = difference, i
            # print("position: %s, direction : %s, difference : %d" %(position, direction, difference))
    print(_min, lifts[index])
else:
    print("Please input in the following format: <lift position> <going up or down> Such as 5U or 10D.")
