def dfs(cnt, now_stress, now_work):
    global res
    res = max(res, now_work)
    if cnt == 24:
        return
    if now_stress + A <= M:
        dfs(cnt + 1, now_stress + A, now_work + B)
    now = now_stress-C
    if now < 0:
        now = 0
    dfs(cnt+1, now, now_work)


A, B, C, M = map(int, input().split())
if A > M:
    res = 0
else:
    res = 0
    dfs(0, 0, 0)
print(res)