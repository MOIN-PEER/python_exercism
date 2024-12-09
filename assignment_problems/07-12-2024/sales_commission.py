"""
Question 2 :
Write a function to calculate the commission of a salesman when sales and the region of
the sales are given as input. The commission is calculated with the rules
as follows:
(a) No commission, if sales < ₹9,000 in Region A
(b) 5.5% commission : of sales < ₹7,000 in Region B and when sales < ₹13,000 in
Region A
(c) 7.5% of sales when sales > = ₹14,000 in Region A and when sales >
= ₹13,000 in Region B.
"""
from django.db.models.fields import return_None


def commission(sales,region):
    # sales_percentage = sales/100
    # print(sales_percentage)
    if region == "A":
        if sales < 9000:
            return "No commission"
        elif sales < 13000:
            return sales * (5.5 / 100)
        else :
            return sales * (7.5 / 100)
    elif region == "B":
        if sales < 7000:
            return sales * (5.5 / 100)
        else :
            return sales * (7.5 / 100)
    else:
        return None

print("Commission for region A/B is",commission(16000,"B"))

