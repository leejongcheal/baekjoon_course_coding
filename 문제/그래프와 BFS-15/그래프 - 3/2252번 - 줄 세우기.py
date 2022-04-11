from collections import defaultdict, deque
N, M = map(int, input().split())
student = [range(1, N+1)]
graph = defaultdict(list)
indegree = [0]*(N)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b - 1] += 1
q = deque()
res = []
for i in range(N):
    if indegree[i] == 0:
        q.append(i+1)
while q:
    now = q.popleft()
    res.append(now)
    for next in graph[now]:
        indegree[next-1] -= 1
        if indegree[next-1] == 0:
            q.append(next)
print(*res)




