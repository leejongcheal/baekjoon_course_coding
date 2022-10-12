from collections import defaultdict
from copy import deepcopy
def fish_move(x, y, d):
    global Map, taste, sx, sy, steps
    for i in range(8):
        nd = (d - i)%8
        dx, dy = steps[nd]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4 and taste[nx][ny] == 0:
            if nx != sx or ny != sy:
                return nx, ny, nd
    return x, y, d

def fishs_move():
    global Map, taste, sx, sy, steps
    New = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in range(8):
                if Map[i][j][d]:
                    x, y, nd = fish_move(i, j, d)
                    New[x][y][nd] += Map[i][j][d]
    Map = New
def shark_moves():
    global step_shark, Map, sx, sy, taste
    """
    이부분을 1로두면 상어가 먹지않더라도 움직이는 경우 제어 못함
    따라서 -1로 두어서 먹이0 제일우선순위 자리 구하는 경우 생각해야함
    """
    Max_cnt = -1
    traked = set()
    for a in range(4):
        for b in range(4):
            for c in range(4):
                cnt = 0
                visit = set()
                x, y = sx, sy
                dx, dy = step_shark[a]
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    visit.add((nx, ny))
                    x, y = nx, ny
                else:
                    continue
                dx, dy = step_shark[b]
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    visit.add((nx, ny))
                    x, y = nx, ny
                else:
                    continue
                dx, dy = step_shark[c]
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    visit.add((nx, ny))
                    x, y = nx, ny
                else:
                    continue
                for x, y in visit:
                    cnt += sum(Map[x][y])
                if cnt > Max_cnt:
                    Max_cnt = cnt
                    traked = [a, b, c]
    x, y = sx, sy
    for d in traked:
        dx, dy = step_shark[d]
        x, y = x + dx, y + dy
        if sum(Map[x][y]):
            taste[x][y] = 3
        Map[x][y] = [0]*8
    return x, y


steps = [(0,-1),(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1,-1)]
step_shark = [(-1, 0),(0, -1),(1, 0),(0, 1)]
M, S = map(int, input().split())
Map = [[[0]*8 for _ in range(4)] for _ in range(4)]
taste = [[0]*4 for _ in range(4)]
for fish_cnt in range(M):
    x, y, d = map(int, input().split())
    Map[x-1][y-1][d-1] += 1
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
cnt = 0
while cnt < S:
    cnt += 1
    initail = deepcopy(Map)
    # 물고기 이동
    fishs_move()
    # 상어 이동
    sx, sy = shark_moves()
    # 냄새 -1
    for i in range(4):
        for j in range(4):
            if taste[i][j] != 0:
                taste[i][j] -= 1
    # 물고기 복사
    for i in range(4):
        for j in range(4):
            for d in range(8):
                Map[i][j][d] += initail[i][j][d]
cnt = 0
for i in range(4):
    for j in range(4):
        cnt += sum(Map[i][j])
print(cnt)