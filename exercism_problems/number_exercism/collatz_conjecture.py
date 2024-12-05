"""
Instructions
The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. If n is even, divide n by 2 to get n / 2.
If n is odd, multiply n by 3 and add 1 to get 3n + 1.
Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1.

example when argument is zero or a negative integer
raise ValueError("Only positive integers are allowed")
"""

def steps(number):
    count = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    for i in range(number + 1):
        if number == 1:
            break
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1

    return count

print("Steps count : ",steps(12))
