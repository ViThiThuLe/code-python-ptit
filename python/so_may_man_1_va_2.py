# so may man 1

# a = input()
# dem = 0
# for i in a:
#     if i == '4' or i == '7':
#         dem += 1
# if dem == 4 or dem == 7:
#     print("YES")
# else:
#     print("NO")


# so may man 2

t = int(input())

while t > 0:
    a = input()
    check = 1
    for i in a:
        if i != '4' and i != '7':
            check = 0
            break
    if (check == 1):
        print("YES")
    else:
        print("NO")
    t -= 1
