import sys
N, T = map(int, sys.stdin.readline().rstrip().split())
Map = [[0]*N for _ in range(N)]
position = []
teleport = []
for _ in range(N):
    s, x, y = map(int, sys.stdin.readline().rstrip().split())
    teleport.append(s)
    position.append([x,y])
for i in range(N):
    for j in range(N):
        xi, yi = position[i]
        xj, yj = position[j]
        diff = abs(xi - xj) + abs(yi - yj)
        if teleport[i] == teleport[j] == 1:
            diff = min(diff, T)
        Map[i][j] = diff
for k in range(N):
    for i in range(N):
        for j in range(N):
            Map[i][j] = min(Map[i][j], Map[i][k] + Map[k][j])
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(Map[a-1][b-1])
