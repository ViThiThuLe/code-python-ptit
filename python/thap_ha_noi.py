def toWer(n, a, b, c):
    if int(n) == 1:
        print(a, " -> ", c)
        return
    toWer(n-1, a, c, b)
    toWer(1, a, b, c)
    toWer(n-1, b, a, c)


a = 'A'
b = 'B'
c = 'C'
n = int(input())
toWer(n, a, b, c)
