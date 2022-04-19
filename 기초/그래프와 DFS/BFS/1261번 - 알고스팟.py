from collections import deque
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
M, N = map(int, input().split())
Map = [list(input()) for _ in range(N)]
INF = int(1e10)
visit = [[INF]*M for _ in range(N)]
visit[0][0] = 0
q = deque()
q.append((0, 0))
next = []
flag = 0
while q:
    same = []
    while q:
        x, y = q.pop()
        if x == N - 1 and y == M - 1:
            flag = 1
            break
        dist = visit[x][y]
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if Map[nx][ny] == '0' and visit[nx][ny] > dist:
                    same.append((nx, ny))
                    visit[nx][ny] = dist
                elif Map[nx][ny] == '1' and visit[nx][ny] > dist + 1:
                    next.append((nx, ny))
                    visit[nx][ny] = dist + 1
    if flag:
        break
    elif same:
        q = same
    else:
        q = next
        next = []
print(visit[N-1][M-1])
