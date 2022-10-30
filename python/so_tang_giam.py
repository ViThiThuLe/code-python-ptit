def ktra(n):
    if len(n) < 3:
        return 0
    else:
        max = 0
        vt = 0
        check = 1
        for i in range(0, len(n)):
            if int(n[i]) > max:
                max = int(n[i])
                vt = i

        for i in range(0, vt):
            if int(n[i]) >= int(n[i + 1]):
                check = 0
                break

        for i in range(vt, len(n) - 1):
            if int(n[i]) <= int(n[i + 1]):
                check = 0
                break

        if check == 1:
            return 1
        return 0


t = int(input())
while t > 0:
    n = input()
    if ktra(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
