def tinh(n):
    tich = 1
    sum = 0
    for i in range(0, len(n)):
        if i % 2 == 0:
            sum += int(n[i])
        else:
            if n[i] == '0':
                continue
            else:
                tich *= int(n[i])
    if tich == 1:
        tich = 0
    print(sum + " " + tich)


t = int(input())
while t > 0:
    n = input()
    tinh(n)
    t -= 1
