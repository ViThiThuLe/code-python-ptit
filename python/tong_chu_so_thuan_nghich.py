def ktra(n):
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    if sum < 10:
        return 0
    else:
        sum = str(sum)
        a = sum[::-1]
        if a != sum:
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
