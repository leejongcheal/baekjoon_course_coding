N, M = map(int, input().split())
x, y, d = map(int, input().split())
Map = [list(map(int, input().split()))]
steps = [(-1, 0),(0,1),(1,0),(0,-1)]
Map[x][y] = 2
res = 1
while 1:
    for i in range(1, 5):
        nd = (d - i) % 4
        dx, dy = steps[nd]
        nx, ny = x + dx, y + dy
        if Map[nx][ny]