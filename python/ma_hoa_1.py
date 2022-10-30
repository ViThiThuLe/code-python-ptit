def mahoa(s):
    a = len(s) - 1
    s1 = ""
    if a == 0:
        return '1' + s
    dem = 1
    for i in range(0, a):
        if i != a - 1:
            if s[i] != s[i+1]:
                s1 += str(dem) + s[i]
                dem = 1
            else:
                dem += 1
        else:
            if s[i] == s[a]:
                s1 += str(dem + 1) + s[i]
            else:
                s1 += str(dem) + s[i] + '1' + s[a]

    return s1


t = int(input())

while t > 0:
    s = input()
    print(mahoa(s))
    t -= 1
