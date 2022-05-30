INF = int(1e10)
N, M = map(int, input().split())
graph = [[INF]*N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
min_dist = INF
x, y = INF, INF
for i in range(N-1):
    for j in range(i+1, N):
        val = 0
        for t in range(N):
            val += min(graph[t][i], graph[t][j])
        if val < min_dist:
            min_dist = val
            x, y = i, j
print(x+1, y+1, min_dist*2)