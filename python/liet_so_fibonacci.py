def fibonacci(n):
    f1 = 1
    f2 = 1

    if (n == 1 or n == 2):
        return 1
    else:
        for i in range(2, n):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn


t = int(input())
while t > 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    sb = ""
    for i in range(a, b + 1):
        sb = sb + str(fibonacci(i)) + " "
    print(sb)
    t -= 1
