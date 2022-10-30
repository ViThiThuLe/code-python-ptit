for i in range(int(input())):
    n, d = input().split()
    n = int(n)
    d = int(d)
    a = [int(i) for i in input().split()]
    b = a[d:n] + a[:d]
    for j in b:
        print(j, end=" ")
    print()
