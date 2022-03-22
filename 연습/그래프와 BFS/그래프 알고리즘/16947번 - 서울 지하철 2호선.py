from collections import deque, defaultdict
import sys
# 순환이 무조건 하나만 나오는 입력값이 주어짐
INF = int(1e10)
N = int(input())
distance = [INF]*(N + 1)
inedge_cnt = [0]*(N+1)
parent = [0]*(N+1)
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    inedge_cnt[a] += 1
    inedge_cnt[b] += 1
q = deque()
# 연결된 간선의수가 1개인것들에 대해서 삭제하면서 연결된 노드 기록
for i in range(1, N+1):
    if inedge_cnt[i] == 1:
        q.append(i)
while q:
    now = q.popleft()
    inedge_cnt[now] -= 1
    for next in graph[now]:
        if parent[next] == 0:
            inedge_cnt[next] -= 1
            if inedge_cnt[next] == 1:
                q.append(next)
            parent[now] = next
for i in range(1, N+1):
    if parent[i] == 0:
        distance[i] = 0
    else:
        p = parent[i]
        cnt = 1
        while parent[p] != 0:
            p = parent[p]
            cnt += 1
        distance[i] = cnt
print(*distance[1:])