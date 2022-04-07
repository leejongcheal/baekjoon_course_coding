steps = [(0, 1),(1, 0),(0, -1),(-1, 0)]
N, M = map(int, input().split())
Map = [[0]*M for _ in range(N)]
cnt = 0
d = 0
x, y = 0, 0
Map[x][y] = 1
flag = 1
while 1:
    dx, dy = steps[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0:
        Map[nx][ny] = 1
        x, y = nx, ny
    else:
        cnt += 1
        d = (d + 1) % 4
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0:
            Map[nx][ny] = 1
            x, y = nx, ny
        else:
            break
print(cnt - 1)



