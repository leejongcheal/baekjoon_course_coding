from collections import deque
import sys
sys.setrecursionlimit(100000000)
def dfs(now, traced):
    global graph, visited, N
    if visited[now] == 1:
        # 사이클이 안생기는 정점으로 조사할 필요가 없는곳
        return 1
    if now in traced:
        index = traced.index(now)
        # print(now, traced)
        if len(traced[index:]) >= 3:
            for t in traced[index:]:
                distance[t] = 0
        return 0
    traced.append(now)
    for next in graph[now]:
        dfs(next, traced)
    traced.pop()
    visited[now] = 1

# 순환이 무조건 하나만 나오는 입력값이 주어짐
from collections import defaultdict
INF = int(1e10)
N = int(input())
distance = [INF]*(N + 1)
visited = [0]*(N + 1) # 1 사이클안생기는정점 2 사이클 생기는 정점
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 사이클 부분 distance 0으로
for i in range(1, N+1):
    if visited[i] != 1:
        dfs(i, [])
no_cyle = deque()
for i in range(1, N+1):
    if distance[i] != 0:
        no_cyle.append(i)
while no_cyle:
    now = no_cyle.popleft()
    flag = 0
    for next in graph[now]:
        if distance[next] != INF:
            distance[now] = min(distance[next] + 1, distance[now])
            flag = 1
    if not flag:
        no_cyle.append(now)
print(*distance[1:])