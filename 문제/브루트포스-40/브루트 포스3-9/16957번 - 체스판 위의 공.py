from collections import deque


def find_chess(Map):
    chess = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0:
                chess.append((Map[i][j], i, j))
    return chess

INF = 1e10
steps = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = [[0]*M for _ in range(N)]
chess = []
for i in range(N):
    for j in range(M):
        chess.append((1, i, j))
while chess:
    temp = [[0]*M for _ in range(N)]
    for cnt, x, y in chess:
        min_val = Map[x][y]
        mx, my = -1, -1
        for dx, dy in steps:
            nx, ny = x + dx,y + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] < min_val:
                min_val = Map[nx][ny]
                mx, my = nx, ny
        if mx != -1:
            temp[mx][my] += cnt
        elif mx == -1:
            res[x][y] += cnt
    chess = find_chess(temp)
for r in res:
    print(*r)