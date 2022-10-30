t = int(input())
while t > 0:
    n = input()
    a = len(n) - 1
    if n[a] == '6' and n[a-1] == '8':
        print("YES")
    else:
        print("NO")
    t -= 1
