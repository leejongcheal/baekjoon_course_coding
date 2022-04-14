from collections import deque, defaultdict
start, end = map(int, input().split())
if start == end:
    res = [start]
else:
    steps = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)]
    n = 578
    N = 2 * n - 1
    Map = [[0] * N for _ in range(N)]
    x, y = n - 1, n - 1
    now = 1
    for k in range(1, n + 1):
        Map[x][y] = now
        now += 1
        for idx, (dx, dy) in enumerate(steps):
            dk = k - 1
            if idx == 0:
                dk = k - 2
            for i in range(dk):
                x += dx
                y += dy
                Map[x][y] = now
                now += 1
        x -= 1
    for i in range(N):
        for j in range(N):
            if Map[i][j] == start:
                x, y = i, j
            if Map[i][j] == end:
                ex, ey = i, j
    res = []
    q = deque()
    q.append((x, y, []))
    visit = defaultdict(int)
    visit[(x, y)] = 1
    while q:
        x, y, tracked = q.popleft()
        if x == ex and y == ey:
            res = [start] + tracked
            break
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] != 0 and visit[(nx, ny)] == 0:
                visit[(nx, ny)] = 1
                q.append((nx, ny, tracked + [Map[nx][ny]]))
print(*res)
