def dao(a):
    b = a[::-1]
    if b == a and len(a) % 2 == 0:
        return True
    return False


def lietke(n):
    s = ""
    for i in range(22, int(n), 2):
        if dao(str(i)) == True:
            check = 0
            for j in range(0, len(str(i))):
                if j == '0' or j == '2' or j == '4' or j == '6' or j == '8':
                    check = 1
                else:
                    check = 0
                    break
            if check == 1:
                s += str(i) + " "
    return s


t = int(input())
while t > 0:
    n = input()
    print(lietke(n))
    t -= 1
