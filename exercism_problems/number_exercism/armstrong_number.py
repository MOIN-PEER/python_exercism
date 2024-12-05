"""
Instructions
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
"""

def is_armstrong_number(number):
    str_num = str(number) #convert to str
    str_length = len(str_num) #length of the str
    armstrong_result = 0 #global value to store result

    for i in str_num: #loop to iterate the value
        i = int(i) #i is str convert to int
        i **= str_length #power
        armstrong_result += i #sum the result

    if armstrong_result == number:
        # return f"{number} is an Armstrong number"
        return True
    # return f"{number} is not an Armstrong number"
    return False

print(is_armstrong_number(153))