from copy import deepcopy


def find_fish(Map, index):
    for i in range(4):
        for j in range(4):
            if Map[i][j] == 0 or Map[i][j] == -1:
                continue
            if Map[i][j][0] == index:
                return i, j
    return -1, -1


def dfs(Map, shark, eat):
    global res
    res = max(res, eat)
    # 물고기 이동
    for index in range(1, 17):
        x, y = find_fish(Map, index)
        if x == -1:
            continue
        d = Map[x][y][1]
        for i in range(8):
            nd = (d + i) % 8
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and Map[nx][ny] != -1:
                if Map[nx][ny] == 0:
                    Map[nx][ny] = [index, nd]
                    Map[x][y] = 0
                else:
                    Map[x][y] = Map[nx][ny]
                    Map[nx][ny] = [index, nd]
                break
    # 상어가 먹을수 있는 물고기에 대해서 dfs 던지기
    x, y, d = shark
    dx, dy = steps[d]
    nx, ny = x + dx, y + dy
    while 0 <= nx < 4 and 0 <= ny < 4:
        if Map[nx][ny] != 0:
            temp = deepcopy(Map)
            temp_shark = (nx, ny, Map[nx][ny][1])
            temp[x][y] = 0
            temp[nx][ny] = -1
            dfs(temp, temp_shark, eat + Map[nx][ny][0])
            # break
        nx += dx
        ny += dy


res = 0
steps = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
Map = []
for _ in range(4):
    x1, d1, x2, d2, x3, d3, x4, d4 = map(int, input().split())
    d1 -= 1
    d2 -= 1
    d3 -= 1
    d4 -= 1
    Map.append([[x1, d1], [x2, d2], [x3, d3], [x4, d4]])
shark = [0, 0, Map[0][0][1]]
eat = Map[0][0][0]
Map[0][0] = -1
dfs(Map, shark, eat)
print(res)
