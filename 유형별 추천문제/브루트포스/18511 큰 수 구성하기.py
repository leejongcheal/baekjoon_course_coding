N, cnt = input().split()
L = list(input().split())
L.sort(reverse=True)
same = 1
res = []
for n in N:
    if n < L[-1] and same:
        if res:
            val = int(res[-1]) - 1
            if val != 0:
                res[-1] = str(val)
                res.append(L[0])
            else:
                res[-1] = L[0]
        same = 0
        continue
    if same:
        for l in L:
                if l == n:
                    res.append(l)
                    break
                elif l < n:
                    res.append(l)
                    same = 0
                    break
    else:
        res.append(L[0])
print("".join(res))
