def perm(L, n):
    global res
    ret = []
    if len(L) < n:
        return
    if n == 1:
        for l in L:
            ret.append([l])
        return ret
    for i in range(len(L)):
        for temp in perm(L[:i] + L[i+1:], n-1):
            ret.append([L[i]]+temp)
    return ret
n = int(input())
k = int(input())
L = [input() for _ in range(n)]
res = set()
ret = perm(L, k)
for r in ret:
    res.add("".join(r))
print(len(res))