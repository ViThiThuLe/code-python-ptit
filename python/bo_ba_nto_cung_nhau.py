import math

l, r = input().split()
l = int(l)
r = int(r)
s = ""

for i in range(l, r - 1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(i, k) == 1:
                s += "(" + str(i) + ", " + str(j) + ", " + str(k) + ")" + "\n"

print(s)
