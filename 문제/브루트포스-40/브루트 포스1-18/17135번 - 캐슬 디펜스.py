from itertools import combinations
from collections import deque
from copy import deepcopy
def bfs(x, y, Map, enemy):
    visit = [[0]*M for _ in range(N)]
    q = deque()
    q.append((x-1, y, 1))
    flag_d = 0
    ds = []
    while q:
        x, y, d = q.popleft()
        if d > D:
            break
        if flag_d and d > flag_d:
            break
        if Map[x][y] == 1:
            flag_d = d
            ds.append((y, x))
        else:
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    q.append((nx, ny, d + 1))
    if ds:
        ds.sort()
        y, x = ds[0]
        enemy.add((x, y))


def move_down(Map, enemy_cnt):
    enemy_cnt -= Map[N-1].count(1)
    for i in range(N-2, -1, -1):
        for j in range(M):
            Map[i+1][j] = Map[i][j]
    for j in range(M):
        Map[0][j] = 0
    return Map, enemy_cnt



def solve(A, Map, D, res):
    enemy_cnt = total_enemy
    re_cnt = 0
    while enemy_cnt > 0:
        # 궁수로 제거하기
        enemy = set()
        for aj in A:
            bfs(N, aj, Map, enemy)

        enemy_cnt -= len(enemy)
        re_cnt += len(enemy)
        for x, y in enemy:
            Map[x][y] = 0
        # 적들 밑으로 이동하기
        Map, enemy_cnt = move_down(Map, enemy_cnt)
    return re_cnt



steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
N, M, D = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
total_enemy = sum([x.count(1) for x in Map])
res = 0
for archers_j in combinations(range(M), 3):
    # print(archers_j)
    temp = deepcopy(Map)
    re_cnt = solve(archers_j, temp, D, res)
    res = max(res, re_cnt)
print(res)
