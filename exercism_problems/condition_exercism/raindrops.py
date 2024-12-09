"""
Instructions
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
"""

def convert(number):
    divisible_3 = number%3==0
    divisible_5 = number%5==0
    divisible_7 = number%7==0
    if (divisible_3 and divisible_5 and divisible_7):
        return "PlingPlangPlong"
    elif(divisible_3 and divisible_5):
        return  "PlingPlang"
    elif(divisible_3 and divisible_7):
        return "PlingPlong"
    elif(divisible_5 and divisible_7):
        return "PlangPlong"
    elif(divisible_3):
        return "Pling"
    elif(divisible_5):
        return "Plang"
    elif(divisible_7):
        return "Plong"
    else:
        return str(number)
# def convert(number):
#     result = []
#     if number % 3 == 0:
#         result.append("Pling")
#     if number % 5 == 0:
#         result.append("Plang")
#     if number % 7 == 0:
#         result.append("Plong")
#     return "".join(result) if result else str(number)

print("Divisible value : ",convert(1))  # "1"
print("Divisible value : ",convert(101)) # "101"
print("Divisible value : ",convert(3)) # "Pling"
print("Divisible value : ",convert(5)) # "Plang"
print("Divisible value : ",convert(7)) # "Plong"
print("Divisible value : ",convert(15)) # "PlingPlang"
print("Divisible value : ",convert(21)) # "PlingPlong"
print("Divisible value : ",convert(35)) # "PlangPlong"
print("Divisible value : ",convert(105)) # "PlingPlangPlong"