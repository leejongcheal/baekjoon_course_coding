from copy import deepcopy
fish_steps = [(0, -1),(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1)]
shark_steps = [(-1, 0),(0, -1),(1, 0),(0, 1)]
def fish_move_check(x, y):
    global fish
    if not (0 <= x < 4 and 0 <= y < 4):
        return 0
    if x == sx and y == sy:
        return 0
    if taste[x][y] > 0:
        return 0
    return 1
def move_shark(d, x, y):
    global cnt, fishs
    dx, dy = shark_steps[d]
    x, y = x + dx, y + dy
    if 0 <= x < 4 and 0 <= y < 4:
        # 위에 묶어서 풀면 안되지 갈순있어야함 범위를 벗어나는 경우를 -1, -1 리턴하도록 변경
        if (x, y) not in fishs:
            cnt += fish_cnt[x][y]
            fishs.add((x, y))
        return x, y
    else:
        return -1, -1
M, S = map(int, input().split())
fish = [[[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(4)] for _ in range(4)]
taste = [[0]*4 for _ in range(4)]
for _ in range(M):
    x, y, d = map(int, input().split())
    fish[x-1][y-1][d-1] += 1
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
for _ in range(S):
    # 물고기 복사
    copy = deepcopy(fish)
    # 물고기 이동
    New = [[[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if fish[x][y][d] != 0:
                    flag = 0
                    for dd in range(8):
                        nd = (d-dd)%8
                        dx, dy = fish_steps[nd]
                        nx, ny = x + dx, y + dy
                        if fish_move_check(nx, ny):
                            flag = 1
                            New[nx][ny][nd] += fish[x][y][d]
                            break
                    # 이동하지 않는경우를 고려하지 않아서 틀림
                    if flag == 0:
                        New[x][y][d] += fish[x][y][d]
    fish = New
    fish_cnt = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            fish_cnt[i][j] = sum(fish[i][j])
    # 상어 이동
    max_cnt = -1 # 0 으로 두고 시작함
    res_d = [] # 만약에 위를 0으로 두었다면 []으로 되서 문제가 생김
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
        if sum(fish[x][y]) != 0:
            taste[x][y] = 3
            fish[x][y] = [0,0,0,0,0,0,0,0]
    sx, sy = x, y
    # 물고기 냄새 -1해주기
    for i in range(4):
        for j in range(4):
            taste[i][j] -= 1
    # 물고기 복사
    for i in range(4):
        for j in range(4):
            for d in range(8):
                fish[i][j][d] += copy[i][j][d]
res = 0
for i in range(4):
    for j in range(4):
        res += sum(fish[i][j])
print(res)