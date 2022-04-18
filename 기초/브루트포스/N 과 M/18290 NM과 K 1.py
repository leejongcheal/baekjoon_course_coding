def dfs(num,tracked,val):
    global res
    if num == K:
        res = max(res, val)
        return
    if val + (K - num)*max_val < res:
        return
    x = y = -1
    if tracked:
        x, y = tracked[-1]
    for i in range(N):
        for j in range(M):
            # if i > x or (i == x and j > y):
            if (i, j) > (x, y) and check(i, j, tracked):
                dfs(num + 1, tracked + [(i,j)], val + Map[i][j])

def check(i, j, tracked):
    if (i, j) in tracked:
        return 0
    for x, y in tracked:
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if nx == i and ny == j:
                return 0
    return 1
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
INF = -(1e10)
N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
max_val = max([max(x) for x in Map])
res = INF
dfs(0,[],0)
print(res)