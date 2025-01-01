"""
Question 1 :
Write a function to sum the digits of a given number until it is reduced to a single digit.
Input : 4321
Output : 1

"""
def sum_of_digit(number):
    sum = 0
    while number > 0 or sum > 9 :
        if number == 0:
            number = sum
            print("number and sum " , number, sum)
            sum = 0
        sum = sum + number % 10
        print("sum",sum)
        number = number // 10
    return sum

print(sum_of_digit(12345))
