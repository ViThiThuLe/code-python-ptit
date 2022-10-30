n = int(input())
a = []
cnt = 0
while cnt < n:
    tmp = [int(i) for i in input().split()]
    for i in tmp:
        a.append(i)
    cnt += len(tmp)

for i in a:
    # doan logic 0
    print(i*(i+1))

    # doan logic 1
    print(2**(i-1) + 1)

    # doan logic 2
    print(i*(i+1)//2-1)
