from collections import deque, defaultdict
INF = int(1e10)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# steps = [(0,1),(1,0),(0,-1),(-1,0)]
M, N = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[INF]*M for _ in range(N)]
flag = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == "C":
            if flag == 0:
                x, y = i, j
                flag += 1
            elif flag:
                ex, ey = i, j
visit[x][y] = 0
q = deque()
for d in range(4):
    q.append((x, y, d, 0))
# 거울갯수를 기준으로 오름차순으로 q 만들어야함
res = -1
while q:
    x, y, d, cnt = q.popleft()
    if x == ex and y == ey:
        res = cnt
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "*":
            if i == d:
                # cnt는 같은데 방향이 다른경우도 생각해줘야함
                if cnt <= visit[nx][ny]:
                    visit[nx][ny] = cnt
                    q.appendleft((nx, ny, d, cnt))
            else:
                if cnt + 1 <= visit[nx][ny]:
                    visit[nx][ny] = cnt + 1
                    q.append((nx, ny, i, cnt + 1))
print(res)