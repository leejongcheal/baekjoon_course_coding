from copy import deepcopy
def hot_wind():
    global Map, wall, steps, next_step, hot, R, C
    for hx, hy, d in hot[::-1]:
        d1, d2 = steps[d]
        x, y = hx + d1, hy + d2
        new = set()
        now = 5
        new.add((x, y))
        while now > 0 and new:
            temp = set()
            for x, y in new:
                Map[x][y] += now
                for dx, dy in next_step[d]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        ddx, ddy = dx - d1, dy - d2
                        dd = 10
                        if ddx != 0 or ddy != 0:
                            dd = steps.index((ddx, ddy))
                        nnx, nny = x + ddx, y + ddy
                        if d not in wall[nnx][nny] and dd not in wall[x][y]:
                            temp.add((nx, ny))
            now -= 1
            new = temp

def bal():
    global Map, wall, next_step, hot, R, C
    steps = [(0,1,0),(1,0,3)]
    temp = deepcopy(Map)
    for i in range(R):
        for j in range(C):
            for dx, dy, d in steps:
                nx, ny = i +dx, j + dy
                if 0 <= nx < R and 0 <= ny <C and d not in wall[i][j]:
                    d = abs(Map[i][j] - Map[nx][ny])//4
                    if Map[i][j] > Map[nx][ny]:
                        d = -1 * d
                    temp[i][j] += d
                    temp[nx][ny] -= d
    Map = temp
def minus1():
    global Map, wall, next_step, hot, R, C
    for j in range(C):
        if Map[0][j] >= 1:
            Map[0][j] -= 1
        if Map[-1][j] >= 1:
            Map[-1][j] -= 1
    for i in range(1, R-1):
        if Map[i][0] >= 1:
            Map[i][0] -= 1
        if Map[i][-1] >= 1:
            Map[i][-1] -= 1

def d_check():
    global Map, check, K
    for x, y in check:
        if not (Map[x][y] >= K):
            return 0
    return 1


R, C, K = map(int, input().split())
check = set()
steps = [(0, 1),(0, -1),(-1, 0),(1, 0)]
next_step = [[(0, 1),(-1, 1),(1, 1)],[(1, -1),(0, -1),(-1, -1)],[(-1, 1),(-1 ,0),(-1, -1)],[(1, 1),(1, 0),(1, -1)]]
hot = [] # x y d
wall = [[[] for _ in range(C)] for _ in range(R)]
Map = []
cnt = 0
for _ in range(R):
    Map.append(list(map(int, input().split())))
for _ in range(int(input())):
    x, y, t = map(int, input().split())
    if t == 0:
        x1, y1 = x-1, y
        d = steps.index((x1 - x, y1 - y))
        wall[x-1][y-1].append(d)
        d = steps.index((x - x1, y - y1))
        wall[x1-1][y1-1].append(d)
    else:
        x1, y1 = x, y + 1
        d = steps.index((x1 - x, y1 - y))
        wall[x-1][y-1].append(d)
        d = steps.index((x - x1, y - y1))
        wall[x1-1][y1-1].append(d)
for i in range(R):
    for j in range(C):
        if Map[i][j] == 5:
            check.add((i, j))
            Map[i][j] = 0
        elif 1 <= Map[i][j] <= 4:
            hot.append((i, j, Map[i][j]-1))
            Map[i][j] = 0
while 1:
    if cnt > 100:
        cnt = 101
        break
    # 온풍기 바람 발생
    hot_wind()
    # 온도조절
    bal()
    # 바깥쪽 -1
    minus1()
    # 초콜릿
    cnt += 1
    # check 하기
    flag = d_check()
    if flag:
        break
print(cnt)