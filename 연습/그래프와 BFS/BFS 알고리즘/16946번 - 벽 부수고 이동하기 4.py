from collections import defaultdict, deque
def bfs(x, y):
    global num
    cnt = 1
    visit[x][y] = num
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == "0" and visit[nx][ny] == 0:
                cnt += 1
                visit[nx][ny] = num
                q.append((nx, ny))
    dist.append(cnt)
    num += 1

steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
visit = [[0]*M for _ in range(N)]
res = [["0"]*M for _ in range(N)]
Map = [list(input()) for _ in range(N)]
num = 1
dist = [0]
wall_list = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == "0" and visit[i][j] == 0:
            bfs(i, j)
        elif Map[i][j] == "1":
            wall_list.append((i,j))
for x, y in wall_list:
    check = []
    cnt = 1
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == '0':
            num = visit[nx][ny]
            if num not in check:
                check.append(num)
                cnt += dist[num]
    res[x][y] = str(cnt%10)
for r in res:
    print("".join(r))