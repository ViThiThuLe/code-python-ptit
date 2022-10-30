import re


def tim_min(s):
    a = re.findall(r'\d+', s)
    min = 9999999
    for i in range(0, len(a)):
        if int(a[i]) < min:
            min = int(a[i])
    return min


def tim_max(s):
    a = re.findall(r'\d+', s)
    max = 0
    for i in range(0, len(a)):
        if int(a[i]) > max:
            max = int(a[i])
    return max


t = int(input())
while t > 0:
    s = input()
    print(tim_max(s))
    t -= 1
