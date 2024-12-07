"""
Instructions

Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.
An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
A scalene triangle has all sides of different lengths.

Note
For a shape to be a triangle at all, all sides have to be of length > 0,
and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
"""


def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b >= c and b + c >= a and a + c >= b) and a + b + c != 0


def equilateral(sides):
    if is_valid_triangle(sides):
        a, b, c = sides
        return a == b == c
    return False


# def equilateral(sides):
#     a = sides[0]
#     b = sides[1]
#     c = sides[2]
#     if (a+b >=c and b+c>=a and a+c>=b)and a+b+c !=0:
#         if (a==b==c):
#             return True
#         else:
#             return False
#     else:
#         return False

def isosceles(sides):
    if is_valid_triangle(sides):
        a, b, c = sides
        return a == b or a == c or b == c
    return False


def scalene(sides):
    if is_valid_triangle(sides):
        a, b, c = sides
        # if (a==b==c) or (a==b or b==c or c==a):
        if equilateral(sides) or isosceles(sides):
            return False
        else:
            return True
    return False


print("Is equilateral : ",equilateral([2, 2, 2])) # True
print("Is equilateral : ",equilateral([0, 0, 0])) # False

print("Is isosceles : ",isosceles([3, 4, 4])) # True
print("Is isosceles : ",isosceles([2, 3, 4])) # False

print("Is scalene : ",scalene([5, 4, 6])) # True
print("Is scalene : ",scalene([4, 3, 3])) # False
print("Is scalene : ",scalene([0.5, 0.4, 0.6])) # True