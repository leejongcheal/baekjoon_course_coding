from collections import deque, defaultdict
from copy import deepcopy
def move_xy(x, y, dx, dy, cx, cy):
    while 1:
        x += dx
        y += dy
        # 벽만난 경우
        if Map[x][y] == "#":
            return x - dx, y - dy, 1
        elif x == cx and y == cy:
            # 벽,구슬만난경우
            if Map[x+dx][y+dy] == "#":
                return x - dx, y - dy, 1
            else:
                return x, y, 0
        # 구멍에 빠진경우
        elif Map[x][y] == "O":
            return -1, -1, 1
def move(rx, ry, bx, by, dx, dy):
    rx, ry, t = move_xy(rx, ry, dx, dy, bx, by)
    if t == 0:
        bx, by, t = move_xy(bx, by, dx, dy, rx, ry)
        rx, ry, t = move_xy(rx, ry, dx, dy, bx, by)
    bx, by, t = move_xy(bx, by, dx, dy, rx, ry)
    return rx, ry, bx, by
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j] == "R":
            rx, ry = i, j
        if Map[i][j] == "B":
            bx, by = i, j
Map[rx][ry] = Map[bx][by] = "."
q = deque()
visit = defaultdict(int)
q.append((rx, ry, bx, by, 0))
visit[(rx, ry, bx, by)] = 1
res = -1
while q:
    rx, ry, bx, by, cnt = q.popleft()
    for dx, dy in steps:
        nrx, nry, nbx, nby = move(rx, ry, bx, by, dx, dy)
        if visit[(nrx, nry, nbx, nby)] != 0:
            continue
        visit[(nrx, nry, nbx, nby)] = 1
        if nrx == -1 and nbx != -1:
            res = cnt + 1
            break
        elif nbx == -1:
            continue
        q.append((nrx, nry, nbx, nby, cnt + 1))
    if res != -1:
        break
print(res)