# TODO
from cs50 import get_float


cents = get_float("Cents owed: ")
cents = int(cents*100.00)


def calculate_change(cents):
    x = 0
    while (cents >= 25):
        cents = cents - 25
        x += 1

    while cents >= 10:
        cents = cents - 10
        x += 1

    while cents >= 5:
        cents = cents - 5
        x += 1

    while cents >= 1:
        cents = cents - 1
        x += 1
    print(x)


calculate_change(cents)
