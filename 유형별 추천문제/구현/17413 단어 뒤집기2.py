L = input()
tag = 0
res = ""
now = ""
for l in L:
    if l == "<":
        tag = 1
        res += now[::-1]
        now = ""
        res += l
    elif l == ">":
        tag = 0
        res += l
    elif l == " ":
        res += now[::-1]
        res += l
        now = ""
    elif tag:
        res += l
    else:
        now += l
res += now[::-1]
print(res)