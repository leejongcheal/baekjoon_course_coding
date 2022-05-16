from collections import deque, defaultdict
def move(x, y, d, cx, cy):
    dx, dy = steps[d]
    while 1:
        if Map[x+dx][y+dy] == "#":
            return x, y, 0
        elif Map[x+dx][y+dy] == "O":
            return x + dx, y + dy, 2
        # 구슬 만난 경우
        elif x + dx == cx and y + dy == cy:
            nx, ny = x + dx, y + dy
            if Map[nx+dx][ny+dy] == "#":
                return x, y, 0
            else:
                return x, y, 1
        x += dx
        y += dy
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j] == "B":
            bx, by = i, j
        if Map[i][j] == "R":
            rx, ry = i, j
Map[rx][ry] = Map[bx][by] = "."
visit = defaultdict(int)
visit[(rx, ry, bx, by)] = 1
q = deque()
q.append((rx, ry, bx, by, 0))
res = -1
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt >= 10:
        break
    for d in range(4):
        nrx, nry, rt = move(rx, ry, d, bx, by)
        if rt == 1:
            nbx, nby, bt = move(bx, by, d, rx, ry)
            nrx, nry, rt = move(rx, ry, d, nbx, nby)
        else:
            nbx, nby, bt = move(bx, by, d, nrx, nry)
        if bt == 2:
            continue
        elif rt == 2:
            res = cnt + 1
            break
        if visit[(nrx, nry, nbx, nby)] == 0:
            visit[(nrx, nry, nbx, nby)] = 1
            q.append((nrx, nry, nbx, nby, cnt + 1))
    if res != -1:
        break
print(res)






