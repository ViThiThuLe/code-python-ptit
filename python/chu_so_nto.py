import math


def nto(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def ktra(n):
    dem1 = 0
    dem2 = 0
    for i in range(0, len(n)):
        if nto(int(n[i])) == 1:
            dem1 += 1
        else:
            dem2 += 1
    if dem1 <= dem2:
        return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    if nto(len(n)) == 1 and ktra(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
