"""
Instruction :

Perfect
A number is perfect when it equals its aliquot sum. For example:

6 is a perfect number because 1 + 2 + 3 = 6
28 is a perfect number because 1 + 2 + 4 + 7 + 14 = 28

Abundant
A number is abundant when it is less than its aliquot sum. For example:

12 is an abundant number because 1 + 2 + 3 + 4 + 6 = 16
24 is an abundant number because 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36

Deficient
A number is deficient when it is greater than its aliquot sum. For example:

8 is a deficient number because 1 + 2 + 4 = 7
Prime numbers are deficient

"""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum_of_number = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(1, number):
            if number % i == 0:
                sum_of_number = sum_of_number + i
        if sum_of_number == number:
            return "perfect"
        elif sum_of_number > number:
            return "abundant"
        else:
            return "deficient"

print(classify(28))
# "perfect"
print(classify(12))
# "abundant"
print(classify(2))
# "deficient"