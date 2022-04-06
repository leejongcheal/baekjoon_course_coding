width_steps = [((0, 1, 0),(0, 1, 0), 0),((0,1, 0),(1, 1, 1), 2)]
height_steps = [((1,0, 0),(1,0, 0), 1),((1,0, 0),(1,1,1), 2)]
diagonal_steps = [((1,1 ,1),(0,1,0), 0),((1,1,1),(1,0,0), 1),((1,1,1),(1,1,1), 2)]
def dfs(x1, y1, x2, y2, shape):
    global res
    if res >= 1000000:
        return
    if x2 == N - 1 and y2 == N - 1:
        res += 1
        return
    if shape == 0:
        now_steps = width_steps
    # 세로
    elif shape == 1:
        now_steps = height_steps
    # 대각선
    else:
        now_steps = diagonal_steps
    for step1, step2, nshape in now_steps:
        dx1, dy1, f1 = step1
        dx2, dy2, f2 = step2
        nx1, ny1 = x1 + dx1, y1 + dy1
        nx2, ny2 = x2 + dx2, y2 + dy2
        if 0 <= nx2 < N and 0 <= ny2 < N\
            and Map[nx2][ny2] != 1:
            if f2 and (Map[x2 + 1][y2] == 1 or Map[x2][y2 + 1] == 1):
                continue
            dfs(nx1, ny1, nx2, ny2, nshape)


N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
dfs(0,0,0,1,0)
print(res)

