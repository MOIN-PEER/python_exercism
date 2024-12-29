"""
Instructions : Dart
Calculate the points scored in a single toss of a Darts game.

Darts is a game where players throw darts at a target.

In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:

Our dart scoreboard with values from a complete miss to a bullseye

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.

"""

def score(x, y):
    square = x**2 + y**2
    if square <=1:
        return 10
    elif square <= 5**2:
        return 5
    elif square <= 10**2:
        return 1
    else:
        return 0

# def score(x, y):
#     r = (x**2+y**2)**0.5
#     return (r<=1)*5+(r<=5)*4+(r<=10)*1

print(score(0, 10))
# 1
print(score(-5, 0))
# 5
print(score(0, 0))
# 10