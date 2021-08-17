import re
import sys
from random import randint

MAX_LIFTS = 5
MAX_FLOORS = 20
DIRECTIONS = ['', 'U', 'D']

DIGIT_WORD_REGEX = re.compile('([0-9]+)([UD])?', re.IGNORECASE)

lifts = {}
while len(lifts) < MAX_LIFTS:
    lifts[str(randint(1, MAX_FLOORS)) + DIRECTIONS[randint(0, 2)]] = 1
lifts = list(lifts.keys())
print("> lift_position = ", lifts)

try:
    u_position, u_direction = DIGIT_WORD_REGEX.search(input("> Enter a request? ")).groups()
    u_position = int(u_position)
    lift_position = ''
    min_distance = None
    for lift_index in range(len(lifts)):
        l_position, l_direction = DIGIT_WORD_REGEX.search(lifts[lift_index]).groups()
        l_position = int(l_position)
        distance = l_position - u_position
        if l_direction == None:
            distance = abs(distance)
        elif l_direction != u_direction:
            if l_direction == 'D':
                distance = l_position + u_position
            elif l_direction == 'U':
                distance = abs(MAX_FLOORS - l_position) + MAX_FLOORS
        elif l_direction == u_direction:
            if l_direction == 'D':
                if l_position > u_position:
                    distance = abs(distance)
                elif l_position < u_position:
                    distance = l_position + u_position + abs(distance)
            if l_direction == 'U':
                if l_position < u_position:
                    distance = abs(distance)
                elif l_position > u_position:
                    distance = l_position + u_position + abs(distance)


        if min_distance == None or min_distance < 0 or min_distance > distance:
            min_distance, lift_position = distance, lift_index

    print("Lift #{} will be comming up to receive you".format(lift_position + 1))
except Exception as e:
    print("Something went wrong")
