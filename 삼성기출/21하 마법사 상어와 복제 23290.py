fish_steps = [(0, -1),(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1)]
shark_steps = [(-1, 0),(0, -1),(1, 0),(0, 1)]
def fish_move_check(x, y):
    global Map
    if not (0 <= x < 4 and 0 <= y < 4):
        return 0
    if x == sx and y == sy:
        return 0
    for t in taste:
        if t in Map[x][y]:
            return 0
    return 1
def move_shark(d, x, y):
    global cnt, fishs
    dx, dy = shark_steps[d]
    x, y = x + dx, y + dy
    if 0 <= x < 4 and 0 <= y < 4 and (x, y) not in fishs:
        cnt += fish[x][y]
        fishs.add((x, y))
        return x, y
    else:
        return -1, -1
M, S = map(int, input().split())
# [1, 2] 냄새, [2, d] 물고기 [3, -1] 상어
Map = [[[] for _ in range(4)] for _ in range(4)]
taste = [[1, 1],[1, 2]]
for _ in range(M):
    x, y, d = map(int, input().split())
    Map[x-1][y-1].append([2, d-1])
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
for _ in range(S):
    # 물고기 복사
    copy = []
    for i in range(4):
        for j in range(4):
            for f, d in Map[i][j]:
                if f == 2:
                    copy.append([i, j, d])
    # 물고기 이동
    New = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for f, d in Map[x][y]:
                if f != 2:
                    New[x][y].append([f, d])
                elif f == 2:
                    for i in range(8):
                        nd = (d - i) % 8
                        dx, dy = fish_steps[nd]
                        nx, ny = x + dx, y + dy
                        if fish_move_check(nx, ny):
                            New[nx][ny].append([2, nd])
                            break
    Map = New
    fish = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            cnt = 0
            for f, d in Map[i][j]:
                if f == 2:
                    cnt += 1
            fish[i][j] = cnt
    # 상어 이동
    max_cnt = 0
    res_d = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                fishs = set()
                cnt = 0
                now = [a, b, c]
                x, y = sx, sy
                x, y = move_shark(a, x, y)
                if x == -1:
                    continue
                x, y = move_shark(b, x, y)
                if x == -1:
                    continue
                x, y = move_shark(c, x, y)
                if x == -1:
                    continue
                if cnt > max_cnt:
                    max_cnt = cnt
                    res_d = now
    x, y = sx, sy
    for d in res_d:
        dx, dy = shark_steps[d]
        x, y = x + dx, y + dy
        temp = Map[x][y]
        Map[x][y] = []
        flag = 0
        for f, d in temp:
            if f != 2:
                Map[x][y].append([f, d])
            elif f == 2:
                if flag == 0:
                    Map[x][y].append([1,3])
                    flag = 1
    sx, sy = x, y
    # 물고기 냄새 -1해주기
    for i in range(4):
        for j in range(4):
            temp = Map[i][j]
            Map[i][j] = []
            for f, d in temp:
                if f == 1:
                    d -= 1
                    if d != 0:
                        Map[i][j].append([f, d])
                else:
                    Map[i][j].append([f, d])
    # 물고기 복사
    for x, y, d in copy:
        Map[x][y].append([2, d])
fish = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        cnt = 0
        for f, d in Map[i][j]:
            if f == 2:
                cnt += 1
        fish[i][j] = cnt
res = sum([sum(x) for x in fish])
print(res)