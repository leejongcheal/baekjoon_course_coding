from itertools import permutations
from copy import deepcopy


def rotation(ro, Map):
    r, c, s = R[ro]
    r -= 1
    c -= 1
    origin = deepcopy(Map)
    sx, sy = r - s, c - s
    while sx != r and sy != c:
        x, y = sx, sy
        d = 0
        dx, dy = steps[d]
        while y != c + s:
            nx, ny = x + dx, y + dy
            Map[nx][ny] = origin[x][y]
            x, y = nx, ny
        d = 1
        dx, dy = steps[d]
        while x != r + s:
            nx, ny = x + dx, y + dy
            Map[nx][ny] = origin[x][y]
            x, y = nx, ny
        d = 2
        dx, dy = steps[d]
        while y != c - s:
            nx, ny = x + dx, y + dy
            Map[nx][ny] = origin[x][y]
            x, y = nx, ny
        d = 3
        dx, dy = steps[d]
        while x != r - s:
            nx, ny = x + dx, y + dy
            Map[nx][ny] = origin[x][y]
            x, y = nx, ny
        sx += 1
        sy += 1
        s -= 1
    return Map


steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = int(1e10)
N, M, K = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]
R = [list(map(int, input().split())) for _ in range(K)]
for comb in permutations(range(K), K):
    temp = deepcopy(origin)
    for ro in comb:
        temp = rotation(ro, temp)
    for t in temp:
        res = min(res, sum(t))
print(res)
