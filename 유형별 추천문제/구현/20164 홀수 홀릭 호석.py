def dfs(L, cnt):
    global max_res, min_res
    n = len(L)
    if n == 1:
        max_res = max(max_res, cnt)
        min_res = min(min_res, cnt)
        return
    elif n == 2:
        next = int(L[0]) + int(L[1])
        next = list(str(next))
        next_cnt = cnt
        for ne in next:
            if ne in odd:
                next_cnt += 1
        dfs(next, next_cnt)
        return
    for f in range(1,n-1):
        for s in range(f+1, n):
            v1 = int("".join(L[:f]))
            v2 = int("".join(L[f:s]))
            v3 = int("".join(L[s:]))
            next = v1 + v2 + v3
            next = list(str(next))
            next_cnt = cnt
            for ne in next:
                if ne in odd:
                    next_cnt += 1
            dfs(next, next_cnt)
L = list(input())
odd = "13579"
cnt = 0
for l in L:
    if l in odd:
        cnt += 1
INF = int(1e10)
max_res = -INF
min_res = INF
dfs(L, cnt)
print(min_res, max_res)