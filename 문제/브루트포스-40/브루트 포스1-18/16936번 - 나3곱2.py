from collections import defaultdict

def dfs(now, tracked):
    global res
    if len(tracked) == N:
        res = tracked
        return
    for n in next[now]:
        if visit[n] == 0:
            visit[n] = 1
            dfs(n, tracked + [n])
            visit[n] = 0
res = 0
N = int(input())
L = list(map(int, input().split()))
next = defaultdict(list)
visit = defaultdict(int)
for now in L:
    if now % 3 == 0 and now // 3 in L:
        next[now].append(now // 3)
    if now*2 in L:
        next[now].append(now*2)
for now in L:
    visit[now] = 1
    dfs(now, [now])
    visit[now] = 0
    if res:
        break
print(*res)