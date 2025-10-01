from math import pi
from random import choice as ch

planets = [
    'Mercury',
    'venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planet = ch(planets)
print("We randomly selected", random_planet)
if random_planet == 'Mercury':
    radius = 2439.7
    print("The radius of Mercury is", radius, "km")
    print("The surface area of Mercury is", 4 * pi * radius**2, "km^2")
elif random_planet == 'Venus':
    radius = 6051.8
    print("The radius of Venus is", radius, "km")
    print("The surface area of Venus is", 4 * pi * radius**2, "km^2")
elif random_planet == 'Earth':
    radius = 6371.0
    print("The radius of Earth is", radius, "km")
    print("The surface area of Earth is", 4 * pi * radius**2, "km^2")
elif random_planet == 'Mars':
    radius = 3389.5
    print("The radius of Mars is", radius, "km")
    print("The surface area of Mars is", 4 * pi * radius**2, "km^2")
elif random_planet == 'Saturn':
    radius = 58232
    print("The radius of Saturn is", radius, "km")
    print("The surface area of Saturn is", 4 * pi * radius**2, "km^2")
else: print("Error occurred!!")