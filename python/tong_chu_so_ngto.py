def nto(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


def chiahet(n):
    a = len(n)
    sum = 0
    for i in range(a):
        sum += int(n[i])
    if nto(sum) == True:
        return True
    return False


t = int(input())
while t > 0:
    n = input()
    if chiahet(n) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
