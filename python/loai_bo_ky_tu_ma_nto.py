import math


def nto(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    for i in s:
        if nto(ord(i)) is False:
            print(i, end='')
    print()
