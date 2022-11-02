for i in range(int(input())):
    s = str(input())
    dem = 0
    while 1:
        dem = dem+1
        if int(s) % 7 == 0:
            print(int(s))
            break
        x = "".join(reversed(s))
        s = int(x)+int(s)
        s = str(s)
        if dem > 1000:
            print(-1)
            break
