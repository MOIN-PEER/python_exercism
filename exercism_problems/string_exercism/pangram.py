"""
Instructions
Your task is to figure out if a sentence is a pangram.

A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
"""

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

# from string import ascii_lowercase
#
# ALPHABET = set(ascii_lowercase)
#
# def is_pangram(string):
#     return ALPHABET.issubset(string.lower())

print(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"))
# True
print(is_pangram(""))
 # False