import re
import sys
from random import randint

MAX_LIFTS = 5
MAX_FLOORS = 20
DIRECTIONS = ['', 'U', 'D']

DIGIT_WORD_REGEX = re.compile('([0-9]+)([UD])?', re.IGNORECASE)

def random_lifts():
    lifts = {}
    while len(lifts) < MAX_LIFTS:
        lifts[str(randint(1, MAX_FLOORS))] = 1
    return [i + DIRECTIONS[randint(0, 2)] for i in lifts.keys()]

"""
   Counts how many steps it would take for the lift to reach
   the destination and based on that lift is selected
"""
def get_nearest_lift(lifts, user_request):
    u_position, u_direction = DIGIT_WORD_REGEX.search(user_request).groups()
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
                    distance = l_position + u_position
            if l_direction == 'U':
                if l_position < u_position:
                    distance = abs(distance)
                elif l_position > u_position:
                    distance = l_position + u_position


        if min_distance == None or min_distance < 0 or min_distance > distance:
            min_distance, lift_position = distance, lift_index

    return lift_position + 1

if __name__ == '__main__':
    lifts = random_lifts()
    print("> lift_position = ", lifts)

    try:
        user_request = input("> Enter a request? ")
        print("Lift #{} will be comming up to receive you".format(get_nearest_lift(lifts, user_request)))
    except Exception as e:
        print("Something went wrong")

