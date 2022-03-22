from collections import deque
import sys
sys.setrecursionlimit(100000000)
def dfs(now, cnt):
    global graph, visited, N
    if visited[now]:
        if cnt - distance[now] >= 3:
            return now
        else:
            return -1
    visited[now] = 1
    distance[now] = cnt
    for next in graph[now]:
        cycleStartNode = dfs(next, cnt + 1)
        if cycleStartNode != -1:
            visited[now] = 2
            if now == cycleStartNode: return -1
            else: return cycleStartNode
    return -1

# 순환이 무조건 하나만 나오는 입력값이 주어짐
from collections import defaultdict
INF = int(1e10)
N = int(input())
distance = [INF]*(N + 1)
visited = [0]*(N + 1) # 1 사이클안생기는정점 2 사이클에 속하는 정점
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 사이클 부분 distance 0으로
dfs(1, 0)


###
q = deque()
for i in range(1, N+1):
    if visited[i] == 2:
        distance[i] = 0
        q.append(i)
    else:
        distance[i] = INF
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == INF:
            distance[next] = distance[now] + 1
            q.append(next)
print(*distance[1:])