"""
Question 5 :

write a function to Obtain the decimal equivalent of a binary number (do not use built in functions)
Input : 1010
Output : 10

"""

def bin_to_dec(bin_num):
    count = 1
    decimal = 0
    bin_num = str(bin_num)

    for i in bin_num :
        print(int(i)*2**(int(len(bin_num))-count))
        decimal = decimal + int(i)*2**(int(len(bin_num))-count)
        # print(decimal)
        count += 1

    return decimal

print(bin_to_dec(1010))
