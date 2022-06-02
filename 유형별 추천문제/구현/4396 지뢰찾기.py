steps = [(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1)]
n = int(input())
Map = [list(input()) for _ in range(n)]
res = [list(input()) for _ in range(n)]
flag = 0
for i in range(n):
    for j in range(n):
        if res[i][j] == "x" and Map[i][j] != "*":
            now = 0
            for dx, dy in steps:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and Map[nx][ny] == "*":
                    now += 1
            res[i][j] = str(now)
        elif res[i][j] == "x" and Map[i][j] == "*" and flag == 0:
            flag = 1
            for x in range(n):
                for y in range(n):
                    if Map[x][y] == "*":
                        res[x][y] = "*"
for r in res:
    print("".join(r))