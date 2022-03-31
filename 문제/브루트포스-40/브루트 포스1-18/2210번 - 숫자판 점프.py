def dfs(x, y, depth, tracked):
    if depth == 6:
        res.add(tuple(tracked))
        return
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, depth + 1, tracked + [Map[nx][ny]])


N = 5
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
res = set()
Map = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        dfs(i, j, 1, [Map[i][j]])
print(len(res))