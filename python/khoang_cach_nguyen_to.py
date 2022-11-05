import math


def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def ktra(n, x):
    dem = 0
    i = 2
    a = []
    a.append(x)
    while dem < n:
        if nto(i) == 1:
            a.append(i)
            dem += 1
        i += 1
    return a


n, x = [int(i) for i in input().split()]
a = ktra(n, x)
b = []

b.append(x)
for i in range(1, n + 1):
    b.append(a[i] + b[i - 1])

for i in range(len(b)):
    print(b[i], end=' ')
