"""
Instructions
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
"""

def is_isogram(word):
    word = word.replace(" ", "").replace("-", "").lower()
    for i in word:
        if i.isalpha():
            if word.count(i) > 1:
                return False
    return True


print(is_isogram("isogram"))
# True
print(is_isogram("hi-oi- "))
# False