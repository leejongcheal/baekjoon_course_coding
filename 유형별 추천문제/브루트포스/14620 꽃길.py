def dfs(i, j,indexs, cnt):
    global res
    if cnt == 3:
        money = 0
        for x, y in indexs:
            money += gold[x][y]
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                money += gold[nx][ny]
        res = min(res, money)
        return
    for x in range(N):
        for y in range(N):
            if (i,j) < (x, y) and Map[x][y] == 0:
                flag = 0
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N and Map[nx][ny] == 0):
                        flag = 1
                        break
                if flag:
                    continue
                Map[x][y] = 1
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    Map[nx][ny] = 1
                dfs(x, y, indexs + [(x, y)], cnt + 1)
                Map[x][y] = 0
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    Map[nx][ny] = 0


steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N = int(input())
Map = [[0]*N for _ in range(N)]
gold = [list(map(int, input().split())) for _ in range(N)]
res = INF = int(1e10)
dfs(-1,-1,[],0)
print(res)