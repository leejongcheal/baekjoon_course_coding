from collections import deque
def dfs(Map, x, y, cnt):
    global res
    if cnt == 2:
        res = max(res, cal(Map))
        return
    for i in range(N):
        for j in range(M):
            if i*10 + j >= 10*x + y and Map[i][j] == 0:
                Map[i][j] = 1
                dfs(Map, i, j, cnt + 1)
                Map[i][j] = 0
def cal(Map):
    visit = dict()
    cnt = 0
    for x, y in white_index:
        visit[(x, y)] = 0
    for x, y in white_index:
        if visit[(x,y)] == 0:
            white_set = set()
            white_set.add((x, y))
            flag = 0
            visit[(x, y)] = 1
            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if Map[nx][ny] == 0:
                            flag = 1
                        elif Map[nx][ny] == 2:
                            if visit[(nx, ny)] == 0:
                                visit[(nx, ny)] = 1
                                white_set.add((nx, ny))
                                q.append((nx, ny))
            if flag == 0:
                cnt += len(white_set)
    return cnt


steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
white_index = []
res = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            white_index.append((i, j))
dfs(Map, 0, 0, 0)
print(res)