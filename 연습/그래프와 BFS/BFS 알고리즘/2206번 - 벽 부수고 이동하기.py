from collections import deque, defaultdict
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
q = deque()
visit = set()
visit.add((0,0,0))
q.append((0,0,0, 1))
res = -1
while q:
    x, y, cracked, dist = q.popleft()
    if x == N - 1 and y == M - 1:
        res = dist
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if Map[nx][ny] == "0" and (nx, ny, cracked) not in visit:
                visit.add((nx, ny, cracked))
                q.append((nx, ny, cracked, dist + 1))
            elif Map[nx][ny] == "1" and cracked == 0:
                nnx, nny = nx + dx, ny + dy
                if 0 <= nnx < N and 0 <= nny < M and Map[nnx][nny] == "0" and \
                        (nnx, nny, cracked + 1) not in visit:
                    visit.add((nnx,nny, cracked+1))
                    q.append((nnx, nny, cracked + 1, dist + 2))
print(res)