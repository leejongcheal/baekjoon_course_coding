steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check(Map, x, y, t):
    for dx, dy in steps:
        nx, ny = x + dx * t, y + dy * t
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == "#":
            a = 1
        else:
            return 0
    return 1


def fill(Map, x, y, t, val):
    for dx, dy in steps:
        nx, ny = x + dx * t, y + dy * t
        Map[nx][ny] = val


def dfs(Map, cross):
    global res
    if len(cross) == 2:
        res = max(res, cross[0][0] * cross[1][0])
        return
    for i in range(N):
        for j in range(M):
            if len(cross) == 1:
                x, y = cross[0][1], cross[0][2]
                if 10 * x + y >= 10 * i + j:
                    continue
            if Map[i][j] == "#":
                t = 0
                while check(Map, i, j, t):
                    area = 1 + 4 * t
                    fill(Map, i, j, t, 0)
                    dfs(Map, cross + [[area, i, j]])
                    t += 1
                for tt in range(t):
                    fill(Map, i, j, tt, "#")


N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
visit2 = [[0] * M for _ in range(N)]
res = 0
dfs(Map, cross=[])
print(res)
