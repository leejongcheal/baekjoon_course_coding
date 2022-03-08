def dfs(time, val):
    if val <= DP[time]:
        return
    DP[time] = val
    for i in range(time, n):
        t, p = L[i]
        if i + t <= n:
            dfs(i + t, p + val)


n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))
DP = [0]*(n+1)
for i in range(n):
    t, p = L[i]
    if i + t <= n:
        dfs(i+t, p)
print(max(DP))