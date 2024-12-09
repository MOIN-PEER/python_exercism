"""
Question 5:
"""
import math
# power = 4**2
# powers = pow(4,2)

def find_gravity(l,T):
    gravity = (4*pow(math.pi,2)*l / pow(T,2))
    return gravity

print("Gravity : ", find_gravity(10,10))

l=10
g = 3.95
T = 2 * math.pi * math.sqrt(l/g)
print(math.ceil(T))
