import json
from random import randint

MAX_LIFTS = 5
MAX_FLOORS = 20
DIRECTIONS = ['', 'U', 'D']

tmp = []
for i in range(0, 60):
    lifts = {}
    while len(lifts) < MAX_LIFTS:
        lifts[str(randint(1, MAX_FLOORS))] = 1
    tmp += [[[(j + DIRECTIONS[randint(0, 2)]) for j in lifts.keys()], (str(randint(1, MAX_FLOORS)) + DIRECTIONS[1:][randint(0, 1)])]]
print(json.dumps(tmp, indent=4))

