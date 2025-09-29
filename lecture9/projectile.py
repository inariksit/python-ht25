###########################################################
## Now we know classes! Modeling cannonball as an object ##
###########################################################


import math
angle = float(input("Initial angle (degrees): "))
vel = float(input("Initial velocity (m/s): "))
height = float(input("Initial height (m): "))

## Conversion to x-velocity and y-velocity
theta = math.radians(angle)
my_xvel = vel * math.cos(theta)
my_yvel = vel * math.sin(theta)



class Projectile:
  def __init__(self,xpos,ypos,xvel,yvel):
    self.xpos = xpos
    self.ypos = ypos
    self.xvel = xvel
    self.yvel = yvel
    self.update_statistics = []

  def update(self, time):
    xpos1 = self.xpos + time * self.xvel
    self.update_statistics.append(f"Updated xpos from {round(self.xpos,0)} to {round(xpos1, 0)}")
    yvel1 = self.yvel - time * 9.8
    ypos1 = self.ypos + time * (self.yvel + yvel1)/2
    self.xpos = xpos1
    self.ypos = ypos1
    self.yvel = yvel1

  def __repr__(self):
    str = f"xpos: {round(self.xpos,0)}, ypos: {round(self.ypos)}"
    return str

  # Added "magic methods": suppose we want to compare
  # a projectile with another, only using xpos as a metric
  def __gt__(self, other):
    return self.xpos > other.xpos


my_cannonball = Projectile(0.0, height, my_xvel, my_yvel)
print(my_cannonball)

for _ in range(100):
  if my_cannonball.ypos < 0:
    break
  my_cannonball.update(0.1)
  print(my_cannonball)

# New cannonball with dummy values
new_cannonball = Projectile(0.0, 100, 30, 40)

print("Thanks to defining __gt__, we can compare two cannonballs!")
print("my_cannonball > new_cannonball:", my_cannonball > new_cannonball)
print("new_cannonball > my_cannonball:", new_cannonball > my_cannonball)