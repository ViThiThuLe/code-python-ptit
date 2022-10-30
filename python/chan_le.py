import math


def ktra(n):
    s = len(n)-1
    check = 1
    sum = 0
    for i in range(0, s):
        a = int(n[i])
        b = int(n[i + 1])
        if math.fabs(a - b) != 2:
            check = 0
            break
        else:
            if i == 0:
                sum += a
            sum += b
    if check == 1 and sum % 10 == 0:
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    n = input()
    ktra(n)
    t -= 1
