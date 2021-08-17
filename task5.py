import re

digit_word_regex = re.compile('([0-9]+)([UD])?', re.IGNORECASE)

for i in [
    (['1U', '4', '3', '13', '18D'], '5D', '4'),
    (['14U', '8U', '2U', '5U', '13D'], '3D', '13D'),
    (['16', '9', '1', '2D', '7U'], '11U', '9'),
    (['2D', '16D', '9', '8D', '7D'], '8U', '9'),
    (['19U', '10D', '12D', '7D', '5'], '3D', '5'),
    (['9U', '4D', '15D', '13U', '1U'], '9D', '15D'),
    (['12U', '11', '5U', '5D', '1U'], '1D', '5D'),
    (['4D', '13', '15', '9', '7'], '11D', '13'),
    (['14U', '18U', '4', '18', '5'], '9U', '5'),
    (['19U', '7', '9', '1U', '17U'], '6D', '7')
]:
    lifts = i[0]
    user_position, user_direction = digit_word_regex.search(i[1]).groups()
    user_position = int(user_position)
    _min, index = None, None
    # print(lifts, i[1], i[2])
    for j in range(len(lifts)):
        # print(lifts[j], j)
        position, direction = digit_word_regex.search(lifts[j]).groups()
        position = int(position)
        cal_diff = abs(position - user_position)
        if direction == None and _min != None and _min > cal_diff:
            # print('if', user_position, position)
            _min, index = cal_diff, j
        elif direction == user_direction:
            # print('elif', direction, position, _min, position > user_position, _min != None and _min > cal_diff)
            if direction == 'U' and position < user_position and ((_min != None and _min > cal_diff) or _min == None):
                # print('elif U', user_position, position)
                _min, index = cal_diff, j
            elif direction == 'D' and position > user_position and ((_min != None and _min > cal_diff) or _min == None):
                # print('elif D', user_position, position)
                _min, index = cal_diff, j
            # elif _min == None and cal_diff != 0:
            #     _min, index = cal_diff, j
        elif _min == None and cal_diff != 0:
            _min, index = cal_diff, j
        ##=> cal_diff = abs(position - user_position)
        ##=> # print(position, direction)
        ##=> # print(lifts[j], position, user_position, cal_diff)
        ##=> if direction == user_direction and _min != None and _min > cal_diff:
        ##=>     print('if')
        ##=>     _min, index = cal_diff, j
        ##=> elif direction == None and _min != None and _min > cal_diff:
        ##=>     print('elif')
        ##=>     _min, index = cal_diff, j
        ##=> elif _min == None and cal_diff != 0:
        ##=>     print('else') #, position, user_position)
        ##=>     if user_direction == 'D' and position > user_position:
        ##=>         _min, index = cal_diff, j
        ##=>     elif user_direction == 'U' and position < user_position:
        ##=>         _min, index = cal_diff, j
        ##=>     elif _min == None:
        ##=>         _min, index = cal_diff, j
        ##=> print('after', _min, index, user_direction, position, user_position)
    print(lifts, i[1], i[2], lifts[index], lifts[index] == i[2])
    print()

