import math


def dao(n):
    a = n
    m = 0
    while n != 0:
        m = m * 10 + n % 10
        n //= 10

    if math.gcd(a, m) == 1:
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    n = int(input())
    dao(n)
    t -= 1
