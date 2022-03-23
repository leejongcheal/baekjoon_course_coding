import heapq
from collections import defaultdict
N, M = map(int, input().split())
labber = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    labber[a] = b
bam = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    labber[a] = b
# cnt , -위치  위치는 내림차순정렬 위해 음수로
q = [(0, -1)]
visit = [-1]*101
visit[1] = 0
while q:
    cnt, now = heapq.heappop(q)
    if -now > 100:
        continue
    if now == -100:
        print(cnt)
        break
    for i in range(1, 7):
        next = -1*now + i
        if bam[next] != 0:
            next = bam[next]
        if labber[next] != 0:
            next = labber[next]
        if next <= 100 and visit[next] == -1:
            visit[next] = cnt + 1
            heapq.heappush(q, (cnt + 1, -1*next))