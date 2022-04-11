def check(x, y):
    tracked = []
    flag = 0  # 나가면 1 못나가면 -1
    while flag == 0:
        tracked.append((x, y))
        dx, dy = steps[Map[x][y]]
        Map[x][y] = 0
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if Map[nx][ny] == 0 or Map[nx][ny] == -1:
                flag = -1
            elif Map[nx][ny] == 1:
                flag = 1
        else:
            flag = 1
        x, y = nx, ny
    for x, y in tracked:
        Map[x][y] = flag


steps = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
# Map 0이면 현재 방문중인 칸 -1 탈출 못하는 칸 1 탈출하는 칸 나머지는 DFS돌리기
for i in range(N):
    for j in range(M):
        if Map[i][j] in steps.keys():
            check(i, j)
res = 0
for m in Map:
    res += m.count(1)
print(res)