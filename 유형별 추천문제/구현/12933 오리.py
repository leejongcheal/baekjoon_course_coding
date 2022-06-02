res = 0
next = dict()
next["q"] = "u"
next["u"] = "a"
next["a"] = "c"
next["c"] = "k"
next["k"] = 0
L = list(input())
remain = []
remain.append(L[0])
for c in L[1:]:
    temp = []
    flag = 0
    for r in remain[::-1]:
        if flag == 0 and next[r] == c:
            if c != "k":
                temp.append(c)
            flag = 1
        elif r != "k":
            temp.append(r)
    remain = temp[::-1]
    if flag == 0:
        remain.append(c)
    res = max(res, len(remain))
if remain:
    res = -1
print(res)