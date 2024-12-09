"""
Question 4 :
To determine and print the minimum number of currency notes of the
denominations: ₹1, ₹5, ₹10, ₹20, ₹50, ₹100, ₹500 and ₹1000 required
to pay any given amount.
"""

# amount = 1786
# >>1000+500+100+100+50+20+10+5+1


def denomination(amount):
    amount_list = []
    for i in range(10):
        if amount / 1000 >= 1:
            amount-=1000
            amount_list.append("1000")
        elif amount / 500 >= 1:
            amount-=500
            amount_list.append("500")

        elif amount / 100 >= 1:
            amount-=100
            amount_list.append("100")

        elif amount / 50 >= 1:
            amount-=50
            amount_list.append("50")

        elif amount / 20 >= 1:
            amount -=20
            amount_list.append("20")

        elif amount / 10 >= 1:
            amount-=10
            amount_list.append("10")

        elif amount / 5 >= 1:
            amount -= 5
            amount_list.append("5")


        elif amount / 1 >= 1:
            amount-=1
            amount_list.append("1")

        else:
            break

    return amount_list

print("Denomination of 1787 : ", denomination(1787))
# Denomination of 1787 :  ['1000', '500', '100', '100', '50', '20', '10', '5', '1', '1']