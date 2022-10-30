from decimal import Decimal, ROUND_HALF_UP


class HocSinh(object):

    def __init__(self, id, name, diem):
        self.name = name
        self.diem = diem
        self.id = id
        tb = 0
        for i in range(len(diem)):
            if i < 2:
                tb += Decimal(str(diem[i]*2))
            else:
                tb += Decimal(str(diem[i]))
        self.tb = Decimal(str(tb/12)).quantize(Decimal('0.1'),
                                               rounding=ROUND_HALF_UP)

    def xeploai(self):
        if self.tb >= 9:
            return "XUAT SAC"
        if self.tb >= 8.0:
            return "GIOI"
        if self.tb >= 7.0:
            return "KHA"
        if self.tb >= 5.0:
            return "TB"
        return "YEU"

    def ma(self):
        id = "HS"
        if self.id < 10:
            id += "0" + str(self.id)
        else:
            id += str(self.id)
        return id

    def __str__(self):
        return self.ma() + " " + self.name + " " + str(self.tb) + " " + self.xeploai()


n = int(input())
a = []
for i in range(n):
    ten = input()
    diem = [float(i) for i in input().split()]
    tmp = HocSinh(i + 1, ten, diem)
    a.append(tmp)

a.sort(key=lambda x: (-x.tb, x.id))
for i in a:
    print(i)
