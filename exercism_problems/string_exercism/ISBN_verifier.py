"""
Instructions
The ISBN-10 verification process is used to validate book identification numbers.
 These normally contain dashes and look like: 3-598-21508-8
 Example
Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
Since the result is 0, this proves that our ISBN is valid.

"""

def is_valid(number):
    number = number.replace("-", "")
    length_number = 10
    total = 0
    for i in number:
        if i.isdigit():
            total += int(i) * length_number
            length_number -= 1
            continue
        if i == 'X' and length_number == 1:
            total += 10
            length_number -= 1
            continue
        return False
    return length_number==0 and  total % 11 == 0

print(is_valid("3-598-21508-8"))
# True
print(is_valid("3-598-P1581-X"))
# False