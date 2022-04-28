from itertools import permutations
from copy import deepcopy
steps = [(0, 1),(1, 0),(0, -1),(-1, 0)]
def rotation_fun(r, c, s):
    ssx, ssy = r - s, c - s
    L = []
    sx, sy = ssx, ssy
    for i in range(N):
        if sx == r and sy == c:
            break
        t = []
        x, y = sx, sy
        for dx, dy in steps:
            for j in range(2*(s - i)):
                x += dx
                y += dy
                t.append(temp[x][y])
        L.append(t[-1:] + t[: -1])
        sx += 1
        sy += 1
    sx, sy = ssx, ssy
    for i in range(N):
        if sx == r and sy == c:
            break
        idx = 0
        t = L[i]
        x, y = sx, sy
        for dx, dy in steps:
            for j in range(2*(s - i)):
                x += dx
                y += dy
                temp[x][y] = t[idx]
                idx += 1
        sx += 1
        sy += 1


N, M, K = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]
rotation = [list(map(int, input().split())) for _ in range(K)]
r = [i for i in range(K)]
res = int(1e10)
for r_order in permutations(r):
    temp = [origin[i][:] for i in range(N)]
    for i in r_order:
        r, c, s = rotation[i]
        r, c = r - 1, c - 1
        rotation_fun(r, c, s)
    res = min(res, min([sum(x) for x in temp]))
print(res)
