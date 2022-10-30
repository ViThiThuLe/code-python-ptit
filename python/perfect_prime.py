import math


def nto(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def ktra(n):
    s = n[::-1]
    if nto(int(s)) != True:
        return False
    else:
        sum = 0
        for i in n:
            if nto(int(i)):
                sum += int(i)
            else:
                return False
        if nto(sum) != True:
            return False
        return True


t = int(input())
while t > 0:
    n = input()
    if nto(int(n)) == True and ktra(n) == True:
        print("Yes")
    else:
        print("No")
    t -= 1
