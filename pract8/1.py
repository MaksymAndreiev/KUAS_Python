import math


def sind(angle):
    return round(math.sin(angle*math.pi/180), 3)


def cosd(angle):
    return round(math.cos(angle * math.pi / 180), 3)


def tand(angle):
    return round(math.tan(angle * math.pi / 180), 3)


print(sind(0))
print(sind(270))
print(cosd(60))
print(tand(45))
