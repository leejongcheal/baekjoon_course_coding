def dfs(x, y, color=0):
    global ans
    if ans == 3:
        return
    ans = max(ans, 1)
    Map[x][y] = color
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == "X":
            ans = 2
            dfs(nx, ny, 1 - color)
        elif 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == color:
            ans = 3
            return

steps = [(-1, 0),(-1, 1),(0, 1),(1, 0),(1, -1),(0, -1)]
N = int(input())
location = []
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] == "X":
            location.append((i, j))
res = 0
for x, y in location:
    if Map[x][y] == "X":
        ans = 1
        dfs(x, y, 0)
        res = max(res, ans)
        if res == 3:
            break
if location:
    print(res)
else:
    print(0)
