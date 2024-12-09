string = "Hello world "
string_format = "beautiful"

print(string)
print(f"{string}")
print('{}'.format(string_format))
print('{1} and {0}'.format(string_format,string)) #indexing

#remove white space : strip, join, split, remove

print(string.strip())
print(string)

print("..........single and double quotes.........")

#single quotes and double quotes :

string_single = 'Hello'
string_double = "Hello"

print(string_single)
print(string_double)

print("..........single inverted and double quotes inverted .........")


# output : "doesn't", '"Isn't," they said.'

string_check = "doesn\'t"
string_double_check = '"Isn\'t," they said.'
print(string_check)
print((string_double_check))

print("..........tab and next line.........")

string_tab = "hello\tworld"
string_new_line = "hello\nworld"
#if we are using 'C:\some\name' like this it will return as :
string_new_check = 'C:\some\name' # to solve use raw string
string_raw = r'C:\some\name'

print(string_tab)
print(string_new_line)
print(string_new_check)
print(string_raw)

print("..........concatenation .........")
# Strings can be concatenated (glued together) with the + operator, and repeated with *

string_mul = 3*"hi"
string_quotes = 'hel' \
                'lo'
string_add = string_mul + " " +  string_quotes

print(string_mul)
print(string_quotes)
print(string_add)

print("..........indexed .........")

string_words = "Python"

print(string_words[0])
print(string_words[-1])
print(string_words[0:-1])
print(string_words[::])
print(string_words[:2])
print(string_words[0:])
print(string_words[-2:])
print(string_words[5])
print("J" + string_words[1::])
