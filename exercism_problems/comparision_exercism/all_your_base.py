"""
Instruction : All Your Base

About Positional Notation
In positional notation, a number in base b can be understood as a linear combination of powers of b.

The number 42, in base 10, means:

(4 × 10¹) + (2 × 10⁰)

The number 101010, in base 2, means:

(1 × 2⁵) + (0 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)

The number 1120, in base 3, means:

(1 × 3³) + (1 × 3²) + (2 × 3¹) + (0 × 3⁰)

Yes. Those three numbers above are exactly the same. Congratulations!

"""

# def base_num(number,base):
#     length = str(number)
#     list = []
#     final = 0
#     for i in length:
#         list.append(i)
#     list.reverse()
#     for index, value in enumerate(list):
#         final = final + (int(value) * pow(base,index))
#     print("final",final)
#
# base_num(1120,3)

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for i in digits:
        if i < 0 or i >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal_value = 0

    for index, digit in enumerate(reversed(digits)):
        decimal_value += digit * (input_base ** index)

    if decimal_value == 0:
        return [0]

    output_digits = []
    while decimal_value > 0:
        remainder = decimal_value % output_base
        output_digits.append(remainder)
        decimal_value //= output_base

    return output_digits[::-1]

print(rebase(2, [1, 0, 1, 0, 1, 0], 10))
 # [4, 2]
print(rebase(2, [1], 10))
 # [1]