import math


def tao(tu, mau):
    return PhanSo(tu, mau)


class PhanSo:
    def __init__(s, x, y):
        s.x = x
        s.y = y

    def toigian(s):
        m = math.gcd(s.x, s.y)
        s.x = s.x/m
        s.y = s.y/m

    def add(s, PhanSo):
        mau = s.y*PhanSo.y
        tu = s.x*PhanSo.y+s.y*PhanSo.x
        return tao(tu, mau)

    def __str__(s):
        return "{}/{}".format(int(s.x), int(s.y))


a, b, c, d = map(int, input().split())
ps1 = PhanSo(a, b)
ps2 = PhanSo(c, d)
ps = ps1.add(ps2)
ps.toigian()
print(ps)
