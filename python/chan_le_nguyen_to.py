import math


def nto(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def ktra(n):
    sum = 0
    check = 0
    for i in range(0, len(n)):
        if i % 2 == 0 and int(n[i]) % 2 == 0:
            check = 1
        elif i % 2 != 0 and int(n[i]) % 2 != 0:
            check = 1
        else:
            check = 0
            break
        sum += int(n[i])

    if check == 1 and nto(sum):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    n = input()
    ktra(n)
    t -= 1
