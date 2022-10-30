def tinh(n):
    sum = 0
    while n > 0:
        sum += 1/n
        n -= 2
    return sum


t = int(input())
while t > 0:
    n = int(input())
    # if n % 2 == 0:
    print("{:.6f}".format(tinh(n)))
    t -= 1
