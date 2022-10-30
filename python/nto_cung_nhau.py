import math

n, k = [int(i) for i in input().split()]
s = ""
dem = 0
if k == 2:
    for i in range(10, 100):
        if math.gcd(n, i) == 1:
            s += str(i) + " "
            dem += 1
        if dem == 10:
            s += "\n"
            dem = 0
elif k == 3:
    for i in range(100, 1000):
        if math.gcd(n, i) == 1:
            s += str(i) + " "
            dem += 1
        if dem == 10:
            s += "\n"
            dem = 0
elif k == 4:
    for i in range(1000, 10000):
        if math.gcd(n, i) == 1:
            s += str(i) + " "
            dem += 1
        if dem == 10:
            s += "\n"
            dem = 0
else:
    for i in range(10000, 100000):
        if math.gcd(n, i) == 1:
            s += str(i) + " "
            dem += 1
        if dem == 10:
            s += "\n"
            dem = 0
print(s)
