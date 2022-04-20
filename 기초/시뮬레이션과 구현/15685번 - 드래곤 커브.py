from collections import defaultdict
steps = [(0,1),(-1,0),(0,-1),(1,0)]
N = int(input())
curve_info = [list(map(int, input().split())) for _ in range(N)]
total_sum = sum([i for i in range(1, N+1)])
total_curve = defaultdict(set) # 해당좌표에 드래곤 커브 idx 넣어주기
idx = 1
for sy, sx, d, g in curve_info:
    curve = defaultdict(int)
    curve[(sx, sy)] = 1
    dx, dy = steps[d]
    nx, ny = sx + dx, sy + dy
    curve[(nx, ny)] = 1
    ex, ey = nx, ny
    for i in range(g):
        L = []
        for x, y in curve.keys():
            nx, ny = y - ey + ex, -x + ex + ey
            L.append((nx, ny))
        for x, y in L:
            curve[(x, y)] = 1
        ex, ey = sy - ey + ex, -sx + ex + ey
    for x, y in curve.keys():
        total_curve[(x, y)].add(idx)
    idx += 1
res = 0
for val in total_curve:
    if sum(val) == total_sum:
        res += 1
print(res)