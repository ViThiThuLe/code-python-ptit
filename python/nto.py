import math


def nto(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


t = int(input())
while t > 0:
    n = int(input())
    k = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            k += 1
    if nto(k):
        print("YES")
    else:
        print("NO")
    t -= 1
