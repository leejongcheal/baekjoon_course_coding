from collections import defaultdict
def dfs(now, tracked):
    global res
    if len(tracked) == 3:
        a, b, c = tracked
        val = len(friend[a]) + len(friend[b]) + len(friend[c]) - 6
        res = min(res, val)
        return
    for next in friend[now]:
        if len(tracked) == 1 and len(friend[next]) > 1 and visit[next] == 0:
            dfs(next, tracked + [next])
        else:
            a = tracked[0]
            if next in friend[a] and visit[next] == 0:
                dfs(next, tracked + [next])


INF = int(1e10)
res = INF
N, M = map(int, input().split())
friend = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
visit = [0]*(N+1)
for i in range(1, N + 1):
    if len(friend[i]) != 0:
        visit[i] = 1
        dfs(i,[i])
if res == INF:
    print(-1)
else:
    print(res)