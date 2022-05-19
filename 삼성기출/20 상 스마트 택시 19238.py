from collections import deque, defaultdict
steps = [(1, 0),(-1, 0),(0, -1),(0, 1)]
def bfs(x, y, target):
    res_d = INF
    res = [(INF, INF)]
    visit = defaultdict(int)
    q = deque()
    visit[(x, y)] = 1
    q.append((x, y, 0))
    while q:
        x, y, d = q.popleft()
        if d > res_d:
            break
        if (x, y) in target:
            res_d = d
            res.append((x, y))
            continue
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == 0 and visit[(nx, ny)] == 0:
                visit[(nx, ny)] = 1
                q.append((nx, ny, d+1))
    res.sort()
    x, y = res[0]
    return x, y, res_d



INF = int(1e10)
N, M, fuel = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
tx, ty = map(int,input().split())
tx -= 1
ty -= 1
passenger = []
destination = dict()
for _ in range(M):
    px, py, dx, dy = map(int, input().split())
    passenger.append((px-1, py-1))
    destination[(px-1, py-1)] = (dx-1, dy-1)
cnt = 0
while cnt < M:
    # 승객 위치 찾기
    tx, ty, d1 = bfs(tx, ty, passenger)
    if d1 == INF or fuel < d1:
        break
    passenger.remove((tx, ty))
    fuel -= d1
    tx, ty, d2 = bfs(tx, ty, [destination[(tx, ty)]])
    if d2 == INF or fuel < d2:
        break
    fuel -= d2
    fuel += d2*2
    cnt += 1
if cnt == M:
    print(fuel)
else:
    print(-1)


