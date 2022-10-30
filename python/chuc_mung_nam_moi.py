n = int(input())
dem = 0
s = []
for i in range(0, n):
    s.append(input())
s1 = []

for i in range(0, n):
    if s[i] not in s1:
        s1.append(s[i])
print(len(s1))
