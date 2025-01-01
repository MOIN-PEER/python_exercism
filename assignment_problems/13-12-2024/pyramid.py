"""
Question 4 :
Write a function to make number of pyramid.

"""

def full_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i -1))
full_pyramid(5)

def half_left(n):
    for i in range(1,n+1):
        print("*" * i )
half_left(5)

def half_right(n):
    for i in range(1,n+1):
        print(" " * (n-i), end='')
        print("*"*i)
half_right(5)


def numeric_pyramid(n):
    for i in range(1,n+1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print numbers
        for j in range(1,i + 1):
            print(j, end=' ')
        print()  # Newline
numeric_pyramid(5)

def symmetric_alphabet_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        # print("*"*i)
        for j in range(1, i + 1):
            print(j,end='')
            # print(chr(64 + j), end='')
        # Print decreasing alphabets
        for j in range(i-1, 0, -1):
            print(j,end='')
            # print(chr(64 + j), end='')
        print()  # Newline after each row

symmetric_alphabet_pyramid(5)

def diamond_alphabet(n):
    # Upper half
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(chr(64 + j), end='')
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end='')
        print()
    # Lower half
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(chr(64 + j), end='')
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end='')
        print()

