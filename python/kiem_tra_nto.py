import math


def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    a = n[-4:]
    if nto(int(a)) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
