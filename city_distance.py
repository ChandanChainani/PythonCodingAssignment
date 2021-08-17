import sys
import math
import re

CITY_FORMAT = re.compile("(\d+.\d+ [NSns], \d+.\d+ [WEwe])")

def signlatlon(direction):
    if (direction.upper() == "N" or direction.upper() == "W"):
        return 1
    return -1

p = math.pi / 180
def calculate(lat1, latd1, log1, logd1, lat2, latd2, log2, logd2):
    R = 1.852 # for km
    lat1 = p * signlatlon(latd1) * lat1
    log1 = p * signlatlon(logd1) * log1
    lat2 = p * signlatlon(latd2) * lat2
    log2 = p * signlatlon(logd2) * log2

    # 180*60/Math.PI
    d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(log1 - log2))

    return d * (180 / math.pi) * 60 * R

if __name__ == "__main__":
    try:
        city1 = input("> City 1: ")
        if CITY_FORMAT.search(city1) == None:
            print("{} is an invalid lat/lon format\nUse DD.DD [NSns], DD.DD [WEwe]".format(city1))
            sys.exit(1)

        city2 = input("> City 2: ")
        if CITY_FORMAT.search(city2) == None:
            print("{} is an invalid lat/lon format\nUse DD.DD [NSns], DD.DD [WEwe]".format(city2))
            sys.exit(1)

        c1lat, c1log = city1.split(',')
        c2lat, c2log = city2.split(',')

        city1lat, city1latsign = c1lat.strip().split(' ')
        city1log, city1logsign = c1log.strip().split(' ')
        city2lat, city2latsign = c2lat.strip().split(' ')
        city2log, city2logsign = c2log.strip().split(' ')

        result = calculate(float(city1lat), city1latsign, float(city1log), city1logsign, float(city2lat), city2latsign, float(city2log), city2logsign)
        print("> Output: City 1 and City 2 are {:.2f} apart".format(result))
    except KeyboardInterrupt:
        print("\nProgram closed")
    except Exception as e:
        print("Something went wrong", e)

