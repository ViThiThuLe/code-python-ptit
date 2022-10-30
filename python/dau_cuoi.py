def ktra(n):
    a = []
    for i in n:
        a.append(i)
    b = len(a)-1
    if a[0] == a[b-1] and a[1] == a[b]:
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    n = input()
    ktra(n)
    t -= 1
