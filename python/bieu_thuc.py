for k in range(int(input())):
    s = input()
    a = []
    b = []
    j = 1
    for i in range(len(s)):
        if s[i] == "(":
            a.append(j)
            b.append(j)
            j += 1
        elif s[i] == ")":
            b.append(a[len(a)-1])
            a.pop()
    for i in b:
        print(i, end=" ")
    print()
