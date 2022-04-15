def solve(Map):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == "w" or Map[i][j] == "W":
                sx, sy = i, j
                if Map[i][j] == "W":
                    cnt += 1
            elif Map[i][j] == "+":
                cnt += 1
    x, y = sx, sy
    for m in move:
        flag = 0
        dx, dy = steps[m]
        nx, ny = x + dx, y + dy
        pre = "."
        if Map[x][y] == "W":
            pre = "+"
        if Map[nx][ny] == ".":
            Map[x][y] = pre
            Map[nx][ny] = "w"
            x, y = nx, ny
        elif Map[nx][ny] == "+":
            Map[x][y] = pre
            Map[nx][ny] = "W"
            x, y = nx, ny
        elif Map[nx][ny] == "b" or Map[nx][ny] == "B":
            pre_box = "w"
            if Map[nx][ny] == "B":
                pre_box = "W"
            nnx, nny = nx + dx, ny + dy
            if Map[nnx][nny] == ".":
                if Map[nx][ny] == "B":
                    cnt += 1
                Map[nnx][nny] = "b"
                Map[nx][ny] = pre_box
                Map[x][y] = pre
                x, y = nx, ny
            elif Map[nnx][nny] == "+":
                if Map[nx][ny] == "B":
                    cnt += 1
                cnt -= 1
                Map[nnx][nny] = "B"
                Map[nx][ny] = pre_box
                Map[x][y] = pre
                x, y = nx, ny
        if cnt == 0:
            break
    res = "complete"
    if cnt != 0:
        res = "incomplete"
    return res


steps = dict()
steps["U"] = (-1, 0)
steps["D"] = (1, 0)
steps["L"] = (0, -1)
steps["R"] = (0, 1)
tc = 0
while 1:
    tc += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    Map = [list(input()) for _ in range(N)]
    move = list(input())
    res = solve(Map)
    print("Game %d: %s"%(tc,res))
    for m in Map:
        print("".join(m))