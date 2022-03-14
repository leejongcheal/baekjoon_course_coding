import sys
input = sys.stdin.readline
from collections import deque, defaultdict
def dfs(v):
    print(v, end=" ")
    for next in graph[v]:
        if visit[next] == 0:
            visit[next] = 1
            dfs(next)
def bfs(v):
    q = deque([V])
    while q:
        now = q.popleft()
        print(now, end=" ")
        for next in graph[now]:
            if visit[next] == 0:
                visit[next] = 1
                q.append(next)


N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
for key in graph:
    graph[key].sort()
visit = [0]*(N+1)
visit[V] = 1
dfs(V)
print()
visit = [0]*(N+1)
visit[V] = 1
bfs(V)