from collections import defaultdict, deque
N = int(input())
indegree = [0]*N
time = []
graph = defaultdict(list)
res = [0]*N
for i in range(N):
    a, *b = map(int, input().split())
    time.append(a)
    indegree[i] = b[0]
    if b[0] == 0:
        continue
    for pre in b[1:]:
        graph[pre - 1].append(i)
q = deque()
for i in range(N):
    if indegree[i] == 0:
        q.append(i)
        res[i] = time[i]
while q:
    now = q.popleft()
    for next in graph[now]:
        res[next] = max(res[next], res[now] + time[next])
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
print(max(res))