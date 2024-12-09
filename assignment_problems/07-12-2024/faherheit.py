"""
Question 6 :
Determine the equivalent fahrenheit temperature of a temperature given in celsius :
C/5 = (F-32) / 9
"""

def fahrenheit_temperature(C):
    fahrenheit = ((9 * C)/5) +32
    return fahrenheit

print(fahrenheit_temperature(20))
    