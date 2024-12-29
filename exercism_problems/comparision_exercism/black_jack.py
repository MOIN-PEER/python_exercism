"""
Instructions :Black Jack
In this exercise you are going to implement some rules of Blackjack, such as the way the game is played and scored.

Note :
In this exercise, A means ace, J means jack, Q means queen, and K means king Jokers are discarded.
A standard French-suited 52-card deck is assumed, but in most versions, several decks are shuffled together for play.

"""

# Functions to help play and score a game of blackjack.

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    face_cards = ['J', 'Q', 'K']
    if card in face_cards:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == card_two_value:
        return card_one, card_two
    elif card_one_value < card_two_value:
        return card_two
    return card_one


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == 1:
        card_one_value = 11
    if card_two_value == 1:
        card_two_value = 11
    total = card_one_value + card_two_value
    if total + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    if card_one_val == 1:
        card_one_val = 11
    if card_two_val == 1:
        card_two_val = 11

    total = card_one_val + card_two_val
    return total == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)
    return card_one == card_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)
    total = card_one + card_two
    return total in (9, 10, 11)

print(value_of_card('K'))
# 10
print(value_of_card('4'))
# 4

print(higher_card('K', '10'))
# ('K', '10')
print(higher_card('4', '6'))
# '6'

print(value_of_ace('6', 'K'))
# 1
print(value_of_ace('7', '3'))
# 11

print(is_blackjack('A', 'K'))
# True
print(is_blackjack('10', '9'))
# False

print(can_split_pairs('Q', 'K'))
# True
print(can_split_pairs('10', 'A'))
# False

print(can_double_down('A', '9'))
# True
print(can_double_down('10', '2'))
# False