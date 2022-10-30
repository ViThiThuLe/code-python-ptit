t = int(input())
while t > 0:
    n, x, m = input().split()
    n = float(n)
    x = float(x)
    m = float(m)
    dem = 0

    while n < m:
        n += n * (x / 100)
        dem += 1

    print(dem)

    t -= 1
