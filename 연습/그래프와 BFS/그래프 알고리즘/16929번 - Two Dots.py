def dfs(x, y, val, traced):
    global visited, Map, steps, N, M
    # if visited[i][j] == 1:
    #     return 1
    if (x,y) in traced:
        # print(22, x, y, traced)
        index = traced.index((x, y))
        if len(traced[index:]) >= 4:
            return 0
        else:
            return 1
    traced.append((x, y))
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == val:
            if not dfs(nx, ny, val, traced):
                return 0
    traced.pop()
    # visited[i][j] = 1
    return 1

steps = [(1,0),(0,1),(-1,0),(0,-1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
flag = 0
# print(dfs(0,0,Map[0][0], []))
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if not dfs(i,j,Map[i][j],[]):
                flag = 1
                break
    if flag:
        break
if flag:
    print("Yes")
else:
    print("No")



