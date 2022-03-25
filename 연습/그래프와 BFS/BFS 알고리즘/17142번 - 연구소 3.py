from itertools import combinations
INF = int(1e10)
steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
M_list = []
blank_cnt = 0
for i in range(N):
    for j in range(N):
        if Map[i][j] == 2:
            M_list.append((i, j))
        elif Map[i][j] == 0:
            blank_cnt += 1
res = INF
for virus in combinations(M_list, M):
    visit = [[-1]*N for _ in range(N)]
    blank = blank_cnt
    for x, y in virus:
        visit[x][y] = 0
    exit = 0
    while blank != 0 and virus:
        next = set()
        for x, y in virus:
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and Map[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    next.add((nx, ny))
                    blank -= 1
                elif 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and Map[nx][ny] == 2:
                    visit[nx][ny] = visit[x][y] + 1
                    next.add((nx, ny))
        virus = next
    # 바이러스를 다 채웠는지 확인
    flag = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1 and Map[i][j] == 0:
                flag = 1
                break
        if flag:
            break
    if not flag:
        cnt = max(max(v) for v in visit)
        res = min(res, cnt)
if res == INF:
    print(-1)
else:
    print(res)