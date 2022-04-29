from collections import deque, defaultdict
from itertools import permutations

steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def bfs(Map):
    global res
    visit = defaultdict(int)
    q = deque()
    visit[(0, 0, 0)] = 1
    q.append((0, 0, 0, 0))
    while q:
        h, x, y, dist = q.popleft()
        # 굳이 조사할 필요가 없으니 끝냄
        if dist >= res:
            return
        if x == 4 and y == 4 and h == 4:
            res = min(res, dist)
            return
        for dh, dx, dy in steps:
            nh, nx, ny = h + dh, x + dx, y + dy
            if 0 <= nh < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if Map[nh][nx][ny] == 1 and visit[(nh, nx, ny)] == 0:
                    visit[(nh, nx, ny)] = 1
                    q.append((nh, nx, ny, dist + 1))


def rotate(A):
    B = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            B[4 - j][i] = A[i][j]
    return B


pans = [[] for _ in range(5)]
# pans 완성
for p in range(5):
    pan = [list(map(int, input().split())) for _ in range(5)]
    pans[p].append(pan)
    temp = pan
    for i in range(3):
        temp = rotate(temp)
        pans[p].append(temp)
    # 중복되는거 제거하기
    check = set()
    t = []
    for sub_pan in pans[p]:
        a = tuple(tuple(sub_pan[i]) for i in range(5))
        pre = len(check)
        check.add(a)
        if pre == len(check):
            t.append(sub_pan)
    for sub_pan in t:
        pans[p].remove(sub_pan)
# 검사할 Map 만들기
res = INF = int(1e10)
for order in permutations(range(5), 5):
    for a in pans[order[0]]:
        for b in pans[order[1]]:
            for c in pans[order[2]]:
                for d in pans[order[3]]:
                    for e in pans[order[4]]:
                        # 출발지와 목적지로 일단 가지치기
                        if a[0][0] == 0 or e[4][4] == 0:
                            continue
                        Map = [a, b, c, d, e]
                        bfs(Map)
if res == INF:
    res = -1
print(res)
