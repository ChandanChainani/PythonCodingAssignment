import re
import sys
# from random import randint

MAX_LIFTS = 5
MAX_FLOORS = 20
DIRECTIONS = ['', 'U', 'D']

DIGIT_WORD_REGEX = re.compile('([0-9]+)([UD])?', re.IGNORECASE)

test_cases = [
    [
        ['0', '1D', '12', '4U', '19D'], '5U', '4U'
    ],
    [
        ['2U', '1U', '18', '5U', '19D'], '4D', '18'
    ],
    [
        ['13', '9', '6U', '18D', '8U'], '1D', '9'
    ],
    [
        ['2D', '17U', '13U', '17', '17D'], '5D', '2D'
    ],
    [
        ['5', '8', '19D', '14', '9D'], '4D', '5'
    ],
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
        [ "13U", "19", "18U", "12D", "7U" ], "8D", '12D'
    ],
    [
        [ "11D", "5", "6U", "4U", "3U" ], "1U", '5'
    ],
    [
        [ "3", "16D", "5D", "9", "14D" ], "6U", '3'
    ],
    [
        [ "18", "5D", "7U", "11U", "8U" ], "6D", '5D'
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
    for lift in lifts:
        l_position, l_direction = DIGIT_WORD_REGEX.search(lift).groups()
        l_position = int(l_position)
        distance = l_position - u_position
        print(u_position, u_direction, l_position, l_direction)
        if l_direction == None:
            # print('beforeIDLE', distance)
            distance = abs(distance)
            # if distance < 0:
            #     distance = abs(distance) + abs(distance)
            # else:
            #     distance = abs(distance)
            # print('afterIDLE', distance)
        elif l_direction != u_direction:
            print('Not Same', distance)
            if l_direction == 'D':
                print('if')
                distance = l_position + u_position
            elif l_direction == 'U':
                print('elif')
                distance = abs(MAX_FLOORS - l_position) + MAX_FLOORS
        elif l_direction == u_direction:
            print('Same', distance)
            if l_direction == 'D':
                if l_position > u_position:
                    print('if')
                    distance = abs(distance)
                elif l_position < u_position:
                    distance = l_position + u_position # + abs(distance)
                    print('elif', l_position, u_position, distance)
            if l_direction == 'U':
                if l_position < u_position:
                    print('if')
                    distance = abs(distance)
                elif l_position > u_position:
                    print('elif')
                    distance = l_position + u_position # + abs(distance)


        print(u_position, l_position, min_distance, distance)
        if min_distance == None or min_distance < 0 or min_distance > distance:
            min_distance, result = distance, lift

    print(result == test[2], result, min_distance)
    print()
    if result != test[2]:
        print('break')
        break
