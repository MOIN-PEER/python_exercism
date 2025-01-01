"""
Question 8 :
Write a function to count the number of vowels, consonants, and special characters in a
given string.

"""

def encode(plain_text):
    result = ""
    for letter in plain_text:
        if letter.isalpha():
            if letter.islower():
                # print(chr(122 - (ord(letter) - 97)))
                result =result + chr(122 - (ord(letter) - 97))
            elif letter.isupper():
                # print(chr(90 - (ord(letter) - 65))
                result = result + chr(90 - (ord(letter) - 65))
        elif letter.isdigit():
            result = result + letter

    encode_text = ""
    for i in range(0, len(result), 5):
        encode_text += result[i:i + 5] + " "

    return encode_text.strip().lower()

def decode(ciphered_text):
    result = ""
    for letter in ciphered_text.replace(" ", ""):  # Remove spaces for decoding
        if letter.isalpha():  # Process alphabetic characters
            if letter.islower():
                result = result + chr(122 - (ord(letter) - 97))  # Reverse lowercase
            elif letter.isupper():
                result = result + chr(90 - (ord(letter) - 65))  # Reverse uppercase
        elif letter.isdigit():  # Keep numbers unchanged
            result += letter
    return result
