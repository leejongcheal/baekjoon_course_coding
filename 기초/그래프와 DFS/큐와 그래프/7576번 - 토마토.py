steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tomato = []
resum = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j))
        elif graph[i][j] == 0:
            resum += 1
time = 0
while resum != 0:
    temp = set()
    for x, y in tomato:
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                temp.add((nx, ny))
    if len(temp) == 0:
        time = -1
        break
    resum -= len(temp)
    for x, y in temp:
        graph[x][y] = 1
    tomato = temp
    time += 1
print(time)
