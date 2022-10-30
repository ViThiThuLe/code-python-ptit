class SinhVien:
    def __init__(self, ten, c, t):
        self.ten = ten
        self.c = c
        self.t = t

    def __str__(self):
        return "{} {} {}".format(self.ten, self.c, self.t)


n = int(input())
a = []
for i in range(n):
    ten = input()
    [c, t] = [int(i) for i in input().split()]
    a.append(SinhVien(ten, c, t))
a.sort(key=lambda x: (-x.c, x.t, x.ten))

for i in a:
    print(i)
