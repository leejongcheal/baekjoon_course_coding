def fill(Map, temp, visit, N, M, x, y):
    steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
    flag = 1
    direction = 0
    while flag:
        flag = 0
        for i in range(2):
            direction = (direction + i) % 4
            dx, dy = steps[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                temp[nx][ny] = Map[x][y]
                visit[nx][ny] = 1
                x, y = nx, ny
                flag = 1
                break


def rotate(Map, N, M):
    visit = [[0]*M for _ in range(N)]
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                fill(Map, temp,visit,N, M, i, j)
    return temp


N, M, R = map(int,input().split())
Map = [list(input().split()) for _ in range(N)]
for _ in range(R):
    Map = rotate(Map, N, M)
for m in Map:
    print(" ".join(m))