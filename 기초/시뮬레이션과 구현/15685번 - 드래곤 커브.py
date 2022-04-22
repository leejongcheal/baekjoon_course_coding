steps = [(1,0),(0,-1),(-1,0),(0,1)]
N = int(input())
curve_info = [list(map(int, input().split())) for _ in range(N)]
total_curve = set()
for sx, sy, d, g in curve_info:
    curve = []
    curve.append((sx, sy))
    dx, dy = steps[d]
    nx, ny = sx + dx, sy + dy
    curve.append((nx, ny))
    ex, ey = nx, ny
    for i in range(g):
        L = []
        for x, y in curve[-2::-1]:
            X, Y = x - ex, y - ey
            nx, ny = -Y + ex, X + ey
            L.append((nx, ny))
        X, Y = sx - ex, sy - ey
        ex, ey = -Y + ex, X + ey
        curve += L
    for now in range(len(curve)):
        x, y = curve[now]
        total_curve.add((x, y))
res = 0
for x, y in total_curve:
    if (x+1, y) in total_curve and (x, y+ 1) in total_curve and (x+1, y+1) in total_curve:
        res += 1
print(res)