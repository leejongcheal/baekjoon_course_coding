from collections import defaultdict, deque
steps = [(-2,-1),(-2, 1),(0,-2),(0, 2),(2, -1),(2, 1)]
N = int(input())
x, y, ex, ey = map(int, input().split())
visit = defaultdict(int)
visit[(x, y)] = 1
q = deque()
q.append((0, x, y))
res = -1
while q:
    cnt, x, y = q.popleft()
    if x == ex and y == ey:
        res = cnt
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and visit[(nx, ny)] == 0:
            visit[(nx, ny)] = 1
            q.append((cnt + 1, nx, ny))
print(res)