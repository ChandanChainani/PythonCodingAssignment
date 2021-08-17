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
    elms = []
    min_distance = None
    for lift_index in range(len(lifts)):
        l_position, l_direction = DIGIT_WORD_REGEX.search(lifts[lift_index]).groups()
        l_position = int(l_position)
        distance = abs(l_position - u_position)

        if l_direction == u_direction or l_direction == None:
            if l_direction == None and (min_distance == None or distance < min_distance):
                # elms.append((distance, lift_index, lifts[lift_index]))
                min_distance, lift_position = distance, lift_index
            elif u_direction == 'D' and l_position > u_position and (min_distance == None or distance < min_distance):
                # elms.append((distance, lift_index, lifts[lift_index]))
                min_distance, lift_position = distance, lift_index
            elif u_direction == 'U' and u_position > l_position and (min_distance == None or distance < min_distance):
                # elms.append((distance, lift_index, lifts[lift_index]))
                min_distance, lift_position = distance, lift_index
    # result = sorted(elms, key=lambda x: x[0])
    # print(result)
    # print(min_distance, lift_position)
    return lifts[lift_position]
    # return lifts[result[0][1]]
    # return 0
        #     print(u_position, l_position, u_direction, distance, min_distance)



            # if u_direction == 'D': # and ((distance > 0 and min_distance > distance) or (distance < 0)):
            #     print('down')
            #     if l_direction == None and l_position < u_position and min_distance < distance:
            #         print('if')
            #         min_distance, lift_position = distance, lift_index
            #     elif l_position > u_position and min_distance > distance:
            #         print('elif')
            #         min_distance, lift_position = distance, lift_index
            # elif u_direction == 'U':
            #     print('up')
            # if l_direction == None:
            #     print('none')



            # if u_direction == 'D' and l_position > u_position and min_distance > distance:
            #     print('down')
            #     min_distance, lift_position = distance, lift_index
            # elif u_direction == 'U' or (l_direction == None and l_position < u_position) and min_distance > distance:
            #     print('up')
            #     min_distance, lift_position = distance, lift_index



            # if u_direction == 'D' and distance > 0 and min_distance > distance:
            #     print('down')
            #     min_distance, lift_position = distance, lift_index
            # elif u_direction == 'U' and (l_position == None or u_position > l_position):
            #     print('up')
            #     min_distance, lift_position = distance, lift_index





            # if u_direction == 'D' and (min_distance != None and min_distance > distance):
            #     print('down')
            #     min_distance, lift_position = distance, lift_index
            # elif u_direction == 'U' and (min_distance != None and min_distance > distance):
            #     print('up')
            #     min_distance, lift_position = distance, lift_index
        #     if u_direction == 'D' and distance > 0 and (min_distance == None or min_distance > distance):
        #         print('down')
        #         min_distance, lift_position = distance, lift_index
        #     elif u_direction == 'U' and distance > 0 and (min_distance == None or min_distance < distance):
        #         print('up')
        #         min_distance, lift_position = distance, lift_index
    # print(lift_position)
    # print(lifts[lift_position])
    # return lifts[lift_position]
    # return 0

if __name__ == '__main__':
    lifts = random_lifts()

    test_cases = [
        [
            ['9', '11U', '7', '3U', '12D'], '4D', '7'
        ],
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
            ['2D', '17U', '13U', '17', '17D'], '5D', '17'
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
            [ "18", "5D", "7U", "11U", "8U" ], "6D", '18'
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
    # test_cases = [
    #     [
    #         ['2U', '1U', '18', '5U', '19D'], '4D', '18'
    #     ],
    #     [
    #         ['13', '9', '6U', '18D', '8U'], '1D', '9'
    #     ],
    #     [
    #         ['2D', '17U', '13U', '17', '17D'], '5D', '17'
    #     ],
    #     [
    #         ['5', '8', '19D', '14', '9D'], '4D', '5'
    #     ],
    #     [
    #         ['1U', '4', '3', '13', '18D'], '5D', '4' # '13' # '4'
    #     ],
    #     [
    #         ['14U', '8U', '2U', '5U', '13D'], '3D', '13D'
    #     ],
    #     [
    #         ['16', '9', '1', '2D', '7U'], '11U', '9' # '7U'
    #     ],
    #     [
    #         ['2D', '16D', '9', '8D', '7D'], '8U', '9'
    #     ],
    #     [
    #         ['19U', '10D', '12D', '7D', '5'], '3D', '5'
    #     ],
    #     [
    #         ['9U', '4D', '15D', '13U', '1U'], '9D', '15D'
    #     ],
    #     [
    #         ['12U', '11', '5U', '5D', '1U'], '1D', '5D'
    #     ],
    #     [
    #         ['4D', '13', '15', '9', '7'], '11D', '13'
    #     ],
    #     [
    #         ['14U', '18U', '4', '18', '5'], '9U', '5'
    #     ],
    #     [
    #         ['19U', '7', '9', '1U', '17U'], '6D', '7'
    #     ],
    #     [
    #         [ "13U", "19", "18U", "12D", "7U" ], "8D", '12D'
    #     ],
    #     [
    #         [ "11D", "5", "6U", "4U", "3U" ], "1U", '5'
    #     ],
    #     [
    #         [ "3", "16D", "5D", "9", "14D" ], "6U", '3'
    #     ],
    #     [
    #         [ "18", "5D", "7U", "11U", "8U" ], "6D", '18'
    #     ],
    #     [
    #         [ "2U", "8", "9U", "4", "3" ], "20D", '8'
    #     ],
    #     [
    #         [ "1", "10U", "6", "3", "20D" ], "16U", '10U'
    #     ],
    #     [
    #         [ "18", "15U", "2", "3U", "13" ], "19U", '18'
    #     ]
    # ]

    # print("> lift_position = ", lifts)

    try:
        total_test_cases = len(test_cases)
        for i in range(total_test_cases):
            test = test_cases[i]
            result = get_nearest_lift(test[0], test[1])
            print(result)
            print("[%d/%d]|[%s] : %s, %s, %s" %(i + 1, total_test_cases, result == test[2], test[0], test[1], test[2]))
            if (result != test[2]):
                print('break')
                break
        # print("Lift #{} will be comming up to receive you".format(get_nearest_lift(lifts, user_request)))
    except Exception as e:
        print("Something went wrong", e)

