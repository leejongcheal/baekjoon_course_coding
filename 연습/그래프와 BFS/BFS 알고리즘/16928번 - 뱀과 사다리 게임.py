from collections import defaultdict, deque
INF = int(1e10)
N, M = map(int, input().split())
labber = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    labber[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    labber[a] = b
visit = [INF]*101
visit[1] = 0
q = deque()
q.append((1, 0))
while q:
    now, dist = q.popleft()
    while labber[now] != 0:
        now = labber[now]
        visit[now] = dist
    if now == 100:
        res = dist
        break
    for i in range(1, 7):
        if now + i <= 100 and visit[now+i] > dist + 1:
            q.append((now+i, dist + 1))
            visit[now+i] = dist + i
print(res)