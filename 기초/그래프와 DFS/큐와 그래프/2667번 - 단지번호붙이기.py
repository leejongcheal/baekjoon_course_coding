from collections import deque
def bfs(x, y, index):
    global N, graph,steps
    q = deque()
    q.append((x, y))
    graph[x][y] = index
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = index
                    cnt += 1
    return cnt

steps = [(1,0),(0,1),(-1,0),(0,-1)]
N = int(input())
graph = list(list(map(int,list(input()))) for _ in range(N))
res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            res.append(bfs(i,j,len(res) + 2))
print(len(res))
for r in sorted(res):
    print(r)