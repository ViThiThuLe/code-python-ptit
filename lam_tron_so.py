for _ in range(int(input())):
    a = int(input())
    b = a
    res = 1
    if a <= 10:
        print(a)
    else:
        while a >= 10:
            h = a % 10
            res *= 10
            if h >= 5:
                b = b+res-h*(res//10)
            else:
                b = b-h*(res//10)
            a = b//res
        print(b)
