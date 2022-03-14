from collections import deque
INF = int(1e10)
steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
N, M = map(int, input().split())
distance = [[INF]*M for _ in range(N)]
graph = [list(map(int, list(input()))) for _ in range(N)]
distance[0][0] = 1
q = deque()
q.append((0,0,1))
while q:
    x, y, dis = q.popleft()
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and distance[nx][ny] > dis + 1:
                distance[nx][ny] = dis + 1
                q.append((nx, ny, dis + 1))
print(distance[N-1][M-1])