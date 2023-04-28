# TODO
from CS50 import get_int
while True:
    user = get_int("Heigh: ")
    if user <= 8 and user >= 1:
        break

for i in range(user):
    print(" "*(user-(i+1)), "#"*(i+1), "  ", "#"*(i+1), sep='')

