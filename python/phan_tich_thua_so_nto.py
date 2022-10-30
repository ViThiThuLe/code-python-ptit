import math


def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def phantich(n):
    i = 2
    a = []
    while n > 1:
        if (n % i == 0):
            n //= i
            a.append(i)
        else:
            i += 1
    return a


t = int(input())
while t > 0:
    n = int(input())
    a = phantich(n)
    vt = 0
    s = "1"
    if nto(n):
        s += " * " + str(n) + "^1"
    else:
        for i in range(0, len(a) - 1):
            if (a[i] != a[i + 1]):
                s += " * " + str(a[i]) + "^" + str(i - vt + 1)
                vt = i + 1
            if i == len(a) - 2:
                s += " * " + str(a[i + 1]) + "^" + str(i - vt + 2)
    print(s)
    t -= 1
