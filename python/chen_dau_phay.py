def commaize(number):
    text = str(number)
    parts = text.split(".")
    ret = ""
    if len(parts) > 1:
        ret = "."
        ret += parts[1]
    for i in range(len(parts[0]) - 1, -1, -1):
        if (len(parts[0]) - i - 1) % 3 == 0 and i != len(parts[0]) - 1:
            ret = "," + ret
        ret = parts[0][i] + ret
    return ret


n = input()
# s1 = s[::-1]
print(commaize(n))
