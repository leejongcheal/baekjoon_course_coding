def calculate(x, y):
    height = []
    now_res = 0
    for width in range(y, N):
        if Map[x][width] != 0:
            height.append(Map[x][width])
            now_res = max(now_res, (width - y + 1)*min(height))
        else:
            return now_res
    return now_res


N = 100
Map = [[0]*N for _ in range(N)]
cnt = int(input())
color_paper = [list(map(int, input().split())) for _ in range(cnt)]
for y, x in color_paper:
    ex = min(x+10, N)
    ey = min(y+10, N)
    for i in range(x, ex):
        for j in range(y, ey):
            Map[i][j] = 1
for i in range(1, N):
    for j in range(N):
        if Map[i][j] != 0 and Map[i-1][j] != 0:
            Map[i][j] = Map[i - 1][j] + 1
res = 100
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            res = max(res, calculate(i, j))
print(res)