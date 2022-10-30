n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
        if i <= n/2-1:
            if j <= n/2-1:
                a[i][j] = j+1
        else:
            if j >= n/2:
                a[i][j] = n-j
        print(a[i][j], end=' ')
    print()
