import math


def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def ktra(n):
    dem = 0
    demnto = 0
    for i in range(0, len(n)):
        if nto(int(n[i])):
            demnto += 1
        else:
            dem += 1
    if nto(len(n)) and demnto > dem:
        return 1
    return 0


t = int(input())
while t > 0:
    n = input()
    if ktra(n):
        print("YES")
    else:
        print("NO")
    t -= 1
