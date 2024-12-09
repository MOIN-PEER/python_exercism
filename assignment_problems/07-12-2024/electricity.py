"""
Question 3 :
 An electricity board charges the following rates to domestic users to
discourage large consumption of energy:
    1. for the first 100 units—₹2 per unit
    2. for the next 200 units—₹3 per unit
    3. Beyond 300 units—₹4.5 per unit
    All users are charged a minimum of ₹ 500.00. If the total cost is more
    than ₹ 2,500.00, then an additional surcharge of 3% of the total cost is
    added to the total cost to determine the final bill.
"""

def electricity(units):
    total_cost = 0
    if units < 100:
        total_cost = units*2
        # return total_cost
    elif units < 300:
        total_cost = 100*2 + (units-100)*3
        # return total_cost
    else:
        total_cost =100*2 + 200*3 + (units-300)*4.5
        # return total_cost

    total_cost = max(total_cost,500) #min total_cost is 500

    if total_cost > 2500:
        print(total_cost)
        total_cost+=total_cost/100 *3
        return total_cost
    else:
        return total_cost


print(electricity(9))
# print(electricity(189))
# print(electricity(289))
# print(electricity(389))
