def ktra(n):
    a = len(n) - 1
    check = 1
    for i in range(0, a):
        if int(n[i]) > int(n[i+1]):
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")


t = int(input())

while t > 0:
    n = input()
    ktra(n)
    t -= 1
