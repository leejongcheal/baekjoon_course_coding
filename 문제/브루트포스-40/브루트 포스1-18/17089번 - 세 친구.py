from collections import defaultdict
def dfs(now, tracked):
    global res
    if len(tracked) == 3:
        val = 0
        a, b, c = tracked
        val += len(friend[a]) + len(friend[b]) + len(friend[c])
        if b in friend[a]:
            val -= 2
        if c in friend[a]:
            val -= 2
        if c in friend[b]:
            val -= 2
        res = min(res, val)
        return
    for next in friend[now]:
        if len(tracked) == 1 and len(friend[next]) > 1:
            dfs(next, tracked + [next])
        else:
            a = tracked[0]
            if next in friend[a]:
                dfs(next, tracked + [next])


INF = int(1e10)
res = INF
N, M = map(int, input().split())
friend = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
for i in range(1, N + 1):
    if len(friend[i]) != 0:
        dfs(i,[i])
if res == INF:
    print(-1)
else:
    print(res)