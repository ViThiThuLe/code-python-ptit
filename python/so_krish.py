
def giaithua(a):
    gt = 1
    for i in range(2, a + 1):
        gt *= i
    return gt


def ktra(n):
    sum = 0
    for i in n:
        sum += giaithua(int(i))

    return str(sum)


t = int(input())
while t > 0:
    n = input()
    if ktra(n) == n:
        print("Yes")
    else:
        print("No")
    t -= 1
