for i in range(int(input())):
    s = input()

    s1 = s.split('\\')
    print(s1[0], end="")
    print("\\..\\", end="")
    print(s1[len(s1)-1], end="")
    print()
