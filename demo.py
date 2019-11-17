from maths.calc import (
    addition,
    subtraction,
    multiplication,
    exponential,
    division,
    square_root,)
print('Addition ', addition(3,2))  # 5
print('Subtraction ', subtraction(3,2))  # 1
print('Multiplication ', multiplication(3,2))  # 6
print('Exponential ', exponential(3,2))  # 9
print('Division ', division(3,2))  # 1.5
print('Square root ', square_root(4))  # 2

from maths.area import (
    area_triangle,
    area_rectangle,
    area_square,
    area_circle,)
print('Triangle', area_triangle(2, 4))  # 4
print('Circle', area_circle(4))  # 50.272
print('Rectangle', area_rectangle(2, 4)) # 8
print('Square', area_square(4))  # 16
