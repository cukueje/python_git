from math import pi
from .calc import exponential, multiplication, division
def area_triangle(base, height):
    return 0.5 * multiplication(base, height)

def area_rectangle(lenght, breath):
    return multiplication(lenght, breath)

def area_square(length1):
   return exponential(length1, 2)

def area_circle(radius):
    return pi * exponential(radius, 2)