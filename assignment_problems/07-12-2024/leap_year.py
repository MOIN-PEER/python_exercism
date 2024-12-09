"""
Question 1 :
 Write a function to find whether a given year is a leap year.
Hint. A year is said to be a leap year if it is either divisible by 4 but not
by 100 or divisible by 400.
"""

def leap_year(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        return True
    return False

print("Yes / No Leap year :",leap_year(2000))
print("Yes / No Leap year :",leap_year(2003))