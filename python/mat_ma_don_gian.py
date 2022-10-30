def ktra(x):
    tmp = ""
    dem = 0
    for i in range(len(x)):
        if x[i] >= '0' and x[i] <= '9':
            if dem == 1:
                dem = 2
            continue
        if dem == 0:
            dem = 1
        if dem == 1:
            tmp += x[i]
        if dem > 1:
            break
    return tmp


def tong(a):
    sum = 0
    for key in range(ord('A'), ord('Z') + 1):
        s = ''
        a = a[: n + 1]
        for i in a:
            s += chr(i ^ key)
        if 'MATLAB' in s:
            for c in s:
                sum += ord(c)
            break
    return sum


n = int(input())
a = []
x = input()
tmp = ktra(x)
while len(a) < n:
    lst = x.split(tmp)
    for i in lst:
        try:
            a.append(int(i))
        except:
            pass
print(tong(a))
