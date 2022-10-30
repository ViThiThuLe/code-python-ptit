def swap(a, b):
    c = a
    a = b
    b = c


def daoso(x, p, q):
    for i in range(0, len(x)):
        if (x[i] == p):
            x[i] = q

    return x


def tong(x1, x2):
    s = ""
    a1 = len(x1)
    a2 = len(x2)
    if a1 < a2:
        swap(x1, x2)

    x2.zfill(a1)
    du = 0
    for i in range(a1 - 1, -1):
        t = int(x1[i]) + int(x2[i]) + du
        if (t >= 10):
            du = 1
            t -= 10
        else:
            du = 0
        s += str(t)

    if du != 0:
        s += '1'
    s = s[::-1]
    return s


t = int(input())
while t > 0:
    p, q = input().split()
    x1 = input()
    x2 = input()
    if int(p) > int(q):
        swap(p, q)
    solon = tong(daoso(x1, p, q), daoso(x2, p, q))
    sobe = tong(daoso(x1, q, p), daoso(x2, q, p))
    print(sobe + " " + solon)
    t -= 1
