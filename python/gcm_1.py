from math import gcd


n = int(input())
a = [int(i) for i in input().split()]

max = 0
for i in range(n):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) > max:
            max = gcd(a[i], a[j])
print(max)
