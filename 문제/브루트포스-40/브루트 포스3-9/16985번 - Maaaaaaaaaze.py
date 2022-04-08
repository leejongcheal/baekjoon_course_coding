from copy import deepcopy
from itertools import permutations
from collections import deque

steps = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


def rotation(Map):
    temp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[i][j] = Map[j][4 - i]
    return temp


origin = []
Map1 = []
Map2 = []
Map3 = []
Map4 = []
Map5 = []
for _ in range(5):
    Map = [list(map(int, input().split())) for _ in range(5)]
    origin.append(Map)
for i in range(5):
    Map = origin[i]
    Map_list = []
    for r in range(4):
        Map = rotation(Map)
        if Map not in Map_list:
            Map_list.append(Map)
    if i == 0:
        Map1 = Map_list
    elif i == 1:
        Map2 = Map_list
    elif i == 2:
        Map3 = Map_list
    elif i == 3:
        Map4 = Map_list
    elif i == 4:
        Map5 = Map_list
Map_set = []
visit_set = []
Maps = [Map1, Map2, Map3, Map4, Map5]
for ch in permutations(range(5), 5):
    for a in Maps[ch[0]]:
        for b in Maps[ch[1]]:
            for c in Maps[ch[2]]:
                for d in Maps[ch[3]]:
                    for e in Maps[ch[4]]:
                        if a[0][0] != 0 and e[4][4] != 0:
                            Map_set.append([a, b, c, d, e])
visit = [[[[0] * 5 for b in range(5)] for c in range(5)] for d in range(len(Map_set))]
q = deque()
res = -1
# print(len(Map_set))
for i in range(len(Map_set)):
    q.append((0, i, 0, 0, 0))
    visit[i][0][0][0] = 1

while q:
    cnt, num, h, x, y = q.popleft()
    if h == x == y == 4:
        res = cnt
        break
    for dh, dx, dy in steps:
        nh, nx, ny = h + dh, x + dx, y + dy
        if 0 <= nh < 5 and 0 <= nx < 5 and 0 <= ny < 5 and Map_set[num][nh][nx][ny] != 0 and visit[num][nh][nx][
            ny] == 0:
            if nh == nx == ny == 4:
                res = cnt + 1
                break
            visit[num][nh][nx][ny] = 1
            q.append((cnt + 1, num, nh, nx, ny))
    if res != -1:
        break
print(res)
