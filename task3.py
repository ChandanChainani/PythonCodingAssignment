import math

# Haversine formula
def deg2rad(deg):
  return deg * (math.pi / 180)

def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
  R = 6371e3; # Radius of the earth in km
  dLat = deg2rad(lat2 - lat1);  # deg2rad below
  dLon = deg2rad(lon2 - lon1);
  a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  d = R * c # Distance in km
  return d

def distance(lat1, lon1, lat2, lon2):
  p = 0.017453292519943295    # math.pi / 180
  a = 0.5 - math.cos((lat2 - lat1) * p)/2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p))/2

  return 12742 * math.asin(math.sqrt(a)) # 2 * R; R = 6371 km

# city1 = input("> City 1: ")
# city2 = input("> City 2: ")
city1 = "51.5074 N, 0.1278 W"
city2 = "48.8566 N, 2.3522 E"
# print(getDistanceFromLatLonInKm(*[float(i.strip().split(' ')[0]) for i in (city1 + city2)]))
print(distance(*[float(i.strip().split(' ')[0]) for i in (city1.split(',') + city2.split(','))]))



from math import radians, cos, sin, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
     
     
# driver code
lat1 = 51.5074
lat2 = 48.8566
lon1 = 0.1278
lon2 =  2.3522
print(distance(lat1, lat2, lon1, lon2), "K.M")



R = 1.852 # km
# R = 6371e3 # metres
lat1 = lat1 * math.pi/180 # φ, λ in radians
lat2 = lat2 * math.pi/180
log1 = (lat2-lat1) * math.pi/180
log2 = (lon2-lon1) * math.pi/180

a = math.sin(log1/2) * math.sin(log1/2) + math.cos(lat1) * math.cos(lat2) * math.sin(log2/2) * math.sin(log2/2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# d = R * c # in metres
# print(d)

i = 200.01
while True:
    d = i * c
    if math.floor(d) > 344:
        break
    i += 0.1
    print(d)
