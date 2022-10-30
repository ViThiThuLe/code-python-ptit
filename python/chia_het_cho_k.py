import math

a, k, n = input().split()
a = int(a)
k = int(k)
n = int(n)
arr = []
if a >= n:
    print("-1")
else:
    for i in range(1, int(n/2) + 1):
        if i % k == 0 and i > a:
            arr.append(i - a)
        if (n-i) % k == 0:
            arr.append(n - i - a)
    arr.sort()
    print(arr)
