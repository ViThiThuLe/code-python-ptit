import re
regex = '[\w\s,:]+'


s = ""
while True:
    try:
        s += input()
    except EOFError:
        break

a = re.findall(regex, s)
for sentence in a:
    b = sentence.lower().split()
    b[0] = b[0].title()
    string = ' '.join(b)
    print(string)
