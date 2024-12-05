
def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value #if one value is float the output will be float


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount // denomination) #truncate (//) always return integer value


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum exchangeable value in foreign currency.

    :param budget: float - the amount of money you plan to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get in foreign currency (in denominations).
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    exchange_money_rate = exchange_money(budget, effective_rate)

    max_value = exchange_money_rate // denomination * denomination #PEDMAS
    return int(max_value)


print("Exchange money : ",exchange_money(127.5, 1.2))
# 106.25
print("Get change : ",get_change(127.5, 120))
# 7.5
print("Get value of bills : ",get_value_of_bills(5, 128))
# 640
print("Get number of bills",get_number_of_bills(127.5, 5))
# 25
print("Get leftover of bills : ",get_leftover_of_bills(127.5, 20))
# 7.5
print("Exchangeable value 1 : ",exchangeable_value(127.25, 1.20, 10, 20))
# 80
print("Exchangeable value 2: ",exchangeable_value(127.25, 1.20, 10, 5))
# 95