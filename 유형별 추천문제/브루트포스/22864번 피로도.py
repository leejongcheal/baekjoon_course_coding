def dfs(cnt, now_stress, now_work):
    global res
    if cnt == 25:
        res = max(res, now_work)
        return
    if now_stress == 0:
        dfs(cnt+1, now_stress+A, now_work+B)
    else:
        if now_stress + A <= M:
            dfs(cnt + 1, now_stress + A, now_work + B)
        dfs(cnt+1, now_stress-C, now_work)

A, B, C, M = map(int, input().split())
if A > M:
    res = 0
else:
    res = 0
    dfs(0, 0, 0)
print(res)