from copy import deepcopy
from collections import defaultdict, deque
def find_pos(Map, index):
    for i in range(4):
        for j in range(4):
            if Map[i][j] == index:
                return i, j
    return -1, -1
def move_fishs(Map, fish_d, sx, sy):
    global steps
    for index in range(1, 17):
        if fish_d[index] == -1:
            continue
        x, y = find_pos(Map, index)
        if x == -1:
            print("error1")
            return
        d = fish_d[index]
        for i in range(8):
            nd = (d+i)%8
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if nx == sx and ny == sy:
                    continue
                Map[nx][ny], Map[x][y] = Map[x][y], Map[nx][ny]
                fish_d[index] = nd
                break
steps= [(-1, 0),(-1, -1),(0, -1),(1, -1),(1, 0),(1, 1),(0, 1),(-1, 1)]
Map = []
fish_d = [-1]*17
for i in range(4):
    L = list(map(int, input().split()))
    fish = [L[j] for j in range(len(L)) if j%2 == 0]
    D = [L[j] for j in range(len(L)) if j%2 == 1]
    Map.append(fish)
    for j in range(4):
        fish_d[fish[j]] = D[j]-1
# 처음 상어 위치 정하기
Max_size = 0
value = Map[0][0]
sx, sy, sd = 0, 0, fish_d[Map[0][0]]
"""
Map[0][0] = 0
fish_d[Map[0][0]] = -1
처럼 사용해서 fish_d[0] = -1 넣어서 오류남 ㅋㅋ
"""
fish_d[Map[0][0]] = -1
Map[0][0] = 0
q = deque()
q.append((Map, fish_d, sx, sy, sd, value))
while q:
    Map, fish_d, sx, sy, sd, value = q.popleft()
    # 물고기 이동
    move_fishs(Map, fish_d, sx, sy)
    # 상어이동 하면서 q에 넣어줘야함
    x, y = sx, sy
    dx, dy = steps[sd]
    while 0 <= x + dx < 4 and 0 <= y + dy < 4:
        x += dx
        y += dy
        if Map[x][y] != 0:
            temp = deepcopy(Map)
            temp[x][y] = 0
            temp_fish_d = deepcopy(fish_d)
            temp_fish_d[Map[x][y]] = -1
            temp_value = value + Map[x][y]
            q.append((temp, temp_fish_d, x, y, fish_d[Map[x][y]], temp_value))
    Max_size = max(Max_size, value)
print(Max_size)