
from math import pi

def circle_area(r):
    if r <0 : 
        raise(ValueError)
    return pi*(r**2)

def circle_perimetre(r):
    if isinstance(r,str):
        raise(TypeError)
    if r < 0  : 
        raise(ValueError)



    return 2*pi*r

