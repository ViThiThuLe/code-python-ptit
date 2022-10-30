def giaima(s):
    n = len(s)
    s1 = ""
    for i in range(0, n):
        if s[i] >= '0' and s[i] <= '9':
            s1 += s[i-1] * int(s[i])
    return s1


t = int(input())
while t > 0:
    s = input()
    print(giaima(s))
    t -= 1
