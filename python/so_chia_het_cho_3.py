def chiahet(n):
    a = len(n)
    sum = 0
    for i in range(a):
        sum += int(n[i])
    if sum % 3 == 0:
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
