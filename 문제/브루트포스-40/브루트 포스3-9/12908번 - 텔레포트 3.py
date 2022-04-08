from collections import defaultdict
import heapq
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
tele_start = []
tele_end = []
for i in range(3):
    a, b, c, d = map(int, input().split())
    tele_start.append([a, b])
    tele_end.append([c, d])
    tele_start.append([c, d])
    tele_end.append([a, b])
DP = defaultdict(int)
DP[(sx, sy)] = 1
q = [(1, sx, sy)]
while q:
    dist, x, y = heapq.heappop(q)
    if x == ex and y == ey:
        DP[(x, y)] = dist
        break
    if dist > DP[(x, y)]:
        continue
    # 바로 끝으로 가는 경우
    next_dist = abs(x - ex) + abs(ey - y)
    if DP[(ex, ey)] == 0 or dist + next_dist < DP[(ex, ey)]:
        DP[(ex, ey)] = dist + next_dist
        heapq.heappush(q, (DP[(ex, ey)], ex, ey))
    # 텔레포트 타러 가는 경우
    for i, n_pos in enumerate(tele_start):
        tx, ty = n_pos
        tele_dist = abs(tx - x) + abs(ty - y)
        nx, ny = tele_end[i]
        next_dist = min(10, abs(tx - nx) + abs(ty - ny))
        if DP[(nx, ny)] == 0:
            DP[(nx, ny)] = dist + tele_dist + next_dist
            heapq.heappush(q, (DP[(nx, ny)], nx, ny))
        elif DP[(nx, ny)] > dist + next_dist + tele_dist:
            DP[(nx, ny)] = dist + tele_dist + next_dist
            heapq.heappush(q, (DP[(nx, ny)], nx, ny))
print(DP[(ex, ey)] - 1)