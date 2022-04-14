L = input().split(":")
res = []
for l in L:
    if l == "":
        continue
    elif len(l) != 4:
        res.append("0"*(4-len(l)) + l)
    else:
        res.append(l)
while len(res) != 8:
    idx = L.index("")
    res.insert(idx,"0000")
print(":".join(res))