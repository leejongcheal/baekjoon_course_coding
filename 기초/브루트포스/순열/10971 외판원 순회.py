def dfs(now, val, cnt):
    global start, min_val, ans, L
    if val + (n - cnt)*min_val > ans:
        return
    if cnt == n and now == start:
        ans = min(ans, val)
        return
    for i in range(n):
        if visit[i] == 0 and L[now][i] != 0:
            visit[i] = 1
            dfs(i, val + L[now][i], cnt + 1)
            visit[i] = 0
        if cnt == n - 1 and i == start and L[now][i] != 0:
            dfs(i, val + L[now][start], cnt + 1)


n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
min_val = 1e10
for i in range(n):
    for j in range(n):
        if L[i][j] != 0:
            min_val = min(min_val, L[i][j])
ans = 1e10
visit = [0]*n
for i in range(n):
    start = i
    visit[i] = 1
    # dfss(i, 0, 0, [i])
    dfs(i, 0, 0)
    visit[i] = 0
print(ans)
