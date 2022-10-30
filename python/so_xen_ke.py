def ktra(n):
    if len(n) % 2 == 0 or n[0] == n[1]:
        return False
    a = n[0]
    for i in range(2, len(n), 2):
        if n[i] != a:
            return False
    return True


t = int(input())
while t > 0:
    n = input()
    if ktra(n) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
