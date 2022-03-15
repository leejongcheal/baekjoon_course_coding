N, M = map(int, input().split())
x, y, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
steps = [(-1, 0),(0,1),(1,0),(0,-1)]
Map[x][y] = 2
res = 1
while 1:
    flag = 0
    for i in range(1, 5):
        nd = (d - i) % 4
        dx, dy = steps[nd]
        nx, ny = x + dx, y + dy
        if Map[nx][ny] == 0:
            x, y, d = nx, ny, nd
            Map[x][y] = 2
            res += 1
            flag = 1
            break
    if flag:
        continue
    # 후진해야하는 경우
    else:
        dx, dy = steps[d]
        px, py = x - dx, y - dy
        if Map[px][py] == 1:
            break
        else:
            x, y = px, py
print(res)