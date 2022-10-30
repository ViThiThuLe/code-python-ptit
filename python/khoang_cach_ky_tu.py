
t = int(input())
while t > 0:
    s1 = input()
    n = len(s1)
    s2 = s1[::-1]
    check = 1
    for i in range(1, n):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
