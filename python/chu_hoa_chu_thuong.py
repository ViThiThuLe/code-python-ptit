s = input()
dem1 = 0
dem2 = 0
for i in s:
    if i >= 'A' and i <= 'Z':
        dem1 += 1
    else:
        dem2 += 1
if dem1 > dem2:
    print(s.upper())
else:
    print(s.lower())
