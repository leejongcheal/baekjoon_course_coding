def spread():
    temp = [[0] * M for _ in range(N)]  # 옮겨진거 넣기
    for x in range(N):
        for y in range(M):
            if Map[x][y] != 0 and Map[x][y] != -1:
                r = Map[x][y]
                c = r // 5
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != -1:
                        temp[nx][ny] += c
                        Map[x][y] -= c
    for i in range(N):
        for j in range(M):
            Map[i][j] += temp[i][j]
def rotation():
    # 위회전
    x, y = up
    pre = 0
    for dx, dy in stepup:
        while 0 <= x + dx < N and 0 <= y + dy < M and Map[x + dx][y + dy] != -1:
            x += dx
            y += dy
            temp = Map[x][y]
            Map[x][y] = pre
            pre = temp
    # 아래 회전
    x, y = down
    pre = 0
    for dx, dy in stepdown:
        while 0 <= x + dx < N and 0 <= y + dy < M and Map[x + dx][y + dy] != -1:
            x += dx
            y += dy
            temp = Map[x][y]
            Map[x][y] = pre
            pre = temp


steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stepup = [(0, 1), (-1, 0), (0, -1), (1, 0)]
stepdown = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
up = down = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == -1:
            if up == 0:
                up = (i, j)
            else:
                down = (i, j)
time = 0
while time < T:
    spread()
    # for m in Map:
    #     print(m)
    # print()
    rotation()
    # for m in Map:
    #     print(m)
    # print()
    time += 1
res = sum([sum(l) for l in Map])
print(res + 2)
