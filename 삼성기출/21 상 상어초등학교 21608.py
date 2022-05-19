from collections import defaultdict
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N = int(input())
Map = [[0]*N for _ in range(N)]
friend = [list(map(int, input().split())) for _ in range(N*N)]
friend_dict = defaultdict(int)
for fr in friend:
    now = fr[0]
    friend_dict[now] = fr[1:]
    res = (-1, -1)
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 0:
                f = b = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if Map[nx][ny] == 0:
                            b += 1
                        elif Map[nx][ny] != 0 and Map[nx][ny] in fr:
                            f += 1
                if (f, b) > res:
                    res = (f, b)
                    can_res = [(i, j)]
                elif (f, b) == res:
                    can_res.append((i, j))
    can_res.sort()
    x, y = can_res[0]
    Map[x][y] = fr[0]
# 완성
comf_res = 0
comf = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        cnt = 0
        now = Map[i][j]
        for dx, dy in steps:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                if Map[nx][ny] in friend_dict[now]:
                    cnt += 1
        comf_res += comf[cnt]
print(comf_res)
