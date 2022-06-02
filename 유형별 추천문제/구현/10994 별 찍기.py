steps = [(0, 1),(1, 0),(0, -1),(-1, 0)]
n = int(input())
N = (n-1)*4+1
Map = [[" "]*N for _ in range(N)]
now, now_N = 0, N
for level in range(n, 0, -1):
    x, y = now, now
    Map[x][y] = "*"
    for dx, dy in steps:
        for i in range(now_N-1):
            x += dx
            y += dy
            Map[x][y] = "*"
    now += 2
    now_N -= 4
for m in Map:
    print("".join(m))