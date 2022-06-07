N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
temp = [m[::] for m in Map]
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
for i in range(N):
    for j in range(M):
        if temp[i][j] == "X":
            cnt = 0
            for dx, dy in steps:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if temp[nx][ny] == ".":
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                Map[i][j] = "."
index = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == "X":
            index.append((i, j))
index.sort()
sx, ex = index[0][0], index[-1][0]
index.sort(key=lambda x:x[1])
sy, ey = index[0][1], index[-1][1]
for i in range(sx, ex+1):
    print("".join(Map[i][sy:ey+1]))
