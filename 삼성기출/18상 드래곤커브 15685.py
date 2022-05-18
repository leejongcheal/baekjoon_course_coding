steps = [(0, 1),(-1, 0),(0, -1),(1, 0)]
size = 101
# size = 10
Map = [[0]*size for _ in range(size)]
N = int(input())
curve = [list(map(int, input().split())) for _ in range(N)]
for x, y, d, g in curve:
    si, sj = y, x
    dx, dy = steps[d]
    ei, ej = si + dx, sj + dy
    c_index = set()
    c_index.add((si, sj))
    c_index.add((ei, ej))
    for _ in range(g):
        next_index = set()
        for i, j in c_index:
            ni = j + ei - ej
            nj = -i + ei + ej
            next_index.add((ni, nj))
        ei, ej = sj + ei - ej, -si + ei + ej
        c_index.update(next_index)
    for i, j in c_index:
        Map[i][j] = 1
res = 0
for i in range(size-1):
    for j in range(size-1):
        if Map[i][j] != 0 and Map[i][j] == Map[i+1][j] == Map[i][j+1] == Map[i+1][j+1]:
            res += 1
print(res)
