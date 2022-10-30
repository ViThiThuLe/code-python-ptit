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
    a, b = input().split()
    a = int(a)
    b = int(b)
    uoc = math.gcd(a, b)

    sum = 0
    while uoc > 0:
        m = uoc % 10
        sum += m
        uoc //= 10

    if nto(sum) == True:
        print("YES")
    else:
        print("NO")

    t -= 1
