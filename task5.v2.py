import re
import sys
# from random import randint

MAX_LIFTS = 5
MAX_FLOORS = 20
DIRECTIONS = ['', 'U', 'D']

DIGIT_WORD_REGEX = re.compile('([0-9]+)([UD])?', re.IGNORECASE)

test_cases = [
    [
        ['1U', '4', '3', '13', '18D'], '5D', '4'
    ],
    [
        ['14U', '8U', '2U', '5U', '13D'], '3D', '13D'
    ],
    [
        ['16', '9', '1', '2D', '7U'], '11U', '9'
    ],
    [
        ['2D', '16D', '9', '8D', '7D'], '8U', '9'
    ],
    [
        ['19U', '10D', '12D', '7D', '5'], '3D', '5'
    ],
    [
        ['9U', '4D', '15D', '13U', '1U'], '9D', '15D'
    ],
    [
        ['12U', '11', '5U', '5D', '1U'], '1D', '5D'
    ],
    [
        ['4D', '13', '15', '9', '7'], '11D', '13'
    ],
    [
        ['14U', '18U', '4', '18', '5'], '9U', '5'
    ],
    [
        ['19U', '7', '9', '1U', '17U'], '6D', '7'
    ],
    [
        [ "13U", "19", "18U", "12D", "7U" ], "8D", '19'
    ],
    [
        [ "11D", "5", "6U", "4U", "3U" ], "1U", '5'
    ],
    [
        [ "3", "16D", "5D", "9", "14D" ], "6U", '3'
    ],
    [
        [ "18", "5D", "7U", "11U", "8U" ], "6D", ''
    ],
    [
        [ "2U", "8", "9U", "4", "3" ], "20D", '8'
    ],
    [
        [ "1", "10U", "6", "3", "20D" ], "16U", '10U'
    ],
    [
        [ "18", "15U", "2", "3U", "13" ], "19U", '18'
    ]
]

for test in test_cases:
    print(test)
    lifts = test[0]
    # print(test[1])
    u_position, u_direction = DIGIT_WORD_REGEX.search(test[1]).groups()
    u_position = int(u_position)
    result = ''
    # print(u_direction, u_position, result)
    min_distance = None
    steps = 0
    for lift in lifts:
        l_position, l_direction = DIGIT_WORD_REGEX.search(lift).groups()
        l_position = int(l_position)
        distance = l_position - u_position

        # if l_direction == None:
        #     print('Lift Idle')
        if l_position > u_position:
            print("Greater")
            if l_direction == None:
                distance = abs(distance)
            elif l_direction != u_direction:
                distance = abs(MAX_FLOORS - l_position + MAX_FLOORS - u_position)
        elif l_position < u_position:
            print("Less")
            if l_direction == None:
                distance = abs(distance)
            elif l_direction != u_direction:
                distance = abs(MAX_FLOORS - l_position + MAX_FLOORS - u_position)

        elif u_direction == l_direction or l_direction == None:
                print("None")
                distance = abs(distance) + abs(distance)
        print("difference", distance, lift)
        # elif l_direction != u_direction or (l_direction == u_direction and l_position > u_position):
        #     print('Different direction', lift)

        #     distance = abs(MAX_FLOORS - l_position) + abs(MAX_FLOORS - u_position)



        if min_distance == None or min_distance > distance:
            print("Update", distance, min_distance, lift)
            min_distance, result = distance, lift















        # if l_direction == u_direction:
        #     print('Same direction')
        #     if u_direction == 'U' and l_position < u_position:
        #         print('Up')
        #     if u_direction == 'D' and l_position > u_position:
        #         print('Down')
        # elif l_direction == None:
        #     print('Lift Idle')
        #     if u_direction == 'U' and l_position < u_position:
        #         print('go Up')
        #     if u_direction == 'D' and l_position > u_position:
        #         print('go Down')
        # elif l_direction == u_direction and (min_distance == None or min_distance > distance):
        #     min_distance, result = distance, lift
        # print("steps", steps, lift)






        # if min_distance != None:
        #     if u_direction == l_direction:
        #         if l_direction == 'D' and min_distance > distance:
        #             print("Down Direction")
        #             min_distance, result = distance, lift
        #         elif l_direction == 'U' and min_distance > distance:
        #             print("Up Direction")
        #             min_distance, result = distance, lift
        #     elif l_direction == None:
        #         if u_direction == 'D' and min_distance > distance:
        #             print("No Direction Down")
        #             min_distance, result = distance, lift
        #         elif u_direction == 'U' and min_distance > distance:
        #             print("No Direction Up")
        #             min_distance, result = distance, lift
        # elif min_distance == None and (l_direction == u_direction or l_direction == None):
        #     print("None", distance, lift)
        #     min_distance, result = distance, lift
        # print("u: %s, l: %s, md: %d, d: %d" %(u_position, l_position, 0 if min_distance == None else min_distance, distance))

    print(min_distance, result, steps)
    print()
    if result != test[2]:
        break
