import math


def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def ktra(n):
    check = 0
    for i in range(0, len(n)):
        if nto(i) == 1 and nto(int(n[i])) == 1:
            check = 1
        elif nto(i) == 0 and nto(int(n[i])) == 0:
            check = 1
        else:
            check = 0
            break
    return check


t = int(input())
while t > 0:
    n = input()
    if ktra(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
