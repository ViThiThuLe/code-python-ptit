def ktra(n):
    for i in range(0, len(n)):
        if n[i] != '0' and n[i] != '1' and n[i] != '2':
            return 0
    return 1


t = int(input())
while t > 0:
    n = input()
    if ktra(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
