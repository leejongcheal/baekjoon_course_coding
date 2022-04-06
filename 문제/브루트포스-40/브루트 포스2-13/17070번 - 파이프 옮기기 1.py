def dfs(x, y, shape):
    global res
    if res >= 1000000:
        return
    if x == N - 1 and y == N - 1:
        res += 1
        return
    # -> 이동
    if shape == 0 or shape == 2:
        nx, ny = x + 0, y + 1
        if ny < N and Map[nx][ny] == 0:
            dfs(nx, ny, 0)
    # | 이동
    if shape == 1 or shape == 2:
        nx, ny = x + 1 , y
        if nx < N and Map[nx][ny] == 0:
            dfs(nx, ny, 1)
    # \ 이동
    nx, ny = x + 1, y + 1
    if nx < N and ny < N and Map[nx][ny] == 0:
        if Map[x+1][y] == 0 and Map[x][y + 1] == 0:
            dfs(nx, ny, 2)
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
dfs(0,1,0)
print(res)

