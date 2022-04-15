from collections import defaultdict, deque




N = 30
Map = [[0]*N for _ in range(N)]
cnt = int(input())
color_paper = [list(map(int, input().split())) for _ in range(cnt)]
for y, x in color_paper:
    ex = min(x+10, N)
    ey = min(y+10, N)
    for i in range(x, ex):
        for j in range(y, ey):
            Map[i][j] = 1
res = 100
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            calculate(i, j)
print(res)