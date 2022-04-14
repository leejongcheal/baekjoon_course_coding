from collections import defaultdict, deque

steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j] == "R":
            rx, ry = i, j
        elif Map[i][j] == "B":
            bx, by = i, j
        elif Map[i][j] == "O":
            ex, ey = i, j
visit = defaultdict(int)
visit[(rx, ry, bx, by)] = 1
q = deque()
q.append((0, rx, ry, bx, by))
res = -1
while q:
    flag = 0
    time, rx, ry, bx, by = q.popleft()
    for dx, dy in steps:
        rflag = bflag = 0
        # 벽또는 멈춘다른공 만나서 멈춘 경우 1 / 구멍에 빠지면 2두기 / 3은 중간에 두공이 같은칸에서 만나는 경우
        nrx, nry = rx, ry
        nbx, nby = bx, by
        while rflag == 0 or bflag == 0:
            if rflag == 0 and Map[nrx + dx][nry + dy] == "#":  # or (bflag == 1 and nrx + dx == nbx and nry + dy == nby):
                rflag = 1
            if bflag == 0 and Map[nbx + dx][nby + dy] == "#":  # or (rflag == 1 and nbx + dx == nrx and nby + dy == nry):
                bflag = 1
            if rflag == 0 and bflag == 1 and nrx + dx == nbx and nry + dy == nby:
                rflag = 1
            if bflag == 0 and rflag == 1 and nbx + dx == nrx and nby + dy == nry:
                bflag = 1
            if rflag == 0 and Map[nrx + dx][nry + dy] == "O":
                rflag = 2
            if bflag == 0 and Map[nbx + dx][nby + dy] == "O":
                bflag = 2
            if rflag == 0:
                nrx += dx
                nry += dy
            if bflag == 0:
                nbx += dx
                nby += dy
            if nrx == nbx and nry == nby:
                rflag = bflag = 3
                break
        if rflag == 2 and bflag != 2:
            res = time + 1
            flag = 1
            break
        elif rflag == bflag == 1 and visit[(nrx, nry, nbx, nby)] == 0:
            visit[(nrx, nry, nbx, nby)] = 1
            q.append((time + 1, nrx, nry, nbx, nby))
    if flag:
        break
print(res)
