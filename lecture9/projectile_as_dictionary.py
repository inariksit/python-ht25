####################################################################
## Before we learned classes: modeling cannonball as a dictionary ##
####################################################################

import math
## Initial values

angle = float(input("Initial angle (degrees): "))
vel = float(input("Initial velocity (m/s): "))
height = float(input("Initial height (m): "))

## Conversion to x-velocity and y-velocity
theta = math.radians(angle)
xvel = vel * math.cos(theta)
yvel = vel * math.sin(theta)

## Our cannonball
my_cannonball = {
    "xpos": 0.0,
    "ypos": height,
    "xvel": xvel,
    "yvel": yvel
}

print(my_cannonball)

def update(p, time):
    xpos1 = p["xpos"] + time * p["xvel"]
    yvel1 = p["yvel"] - time * 9.8
    ypos1 = p["ypos"] + time * (p["yvel"] + yvel1)/2
    p["xpos"] = xpos1
    p["ypos"] = ypos1
    p["yvel"] = yvel1

for _ in range(100):
    update(my_cannonball, 0.01)
    if my_cannonball["ypos"] < 0:
        break
    print(my_cannonball)