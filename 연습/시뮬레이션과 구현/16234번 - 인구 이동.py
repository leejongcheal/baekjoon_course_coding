from collections import deque


def bfs(sx, sy):
    index = len(human_avc)
    human_set = set()
    q = deque()
    sum_human = Map[sx][sy]
    q.append((sx, sy))
    visit[sx][sy] = index
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 \
                and L <= abs(Map[x][y] - Map[nx][ny]) <= R:
                sum_human += Map[nx][ny]
                visit[nx][ny] = index
                cnt += 1
                q.append((nx, ny))
    if cnt > 1:
        human_avc.append(int(sum_human/cnt))
    else:
        visit[sx][sy] = -1


steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, L, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
while 1:
    visit = [[-1] * N for _ in range(N)]
    human_avc = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                bfs(i, j)
    if len(human_avc) == 0:
        break
    res += 1
    for i in range(N):
        for j in range(N):
            if visit[i][j] != -1:
                Map[i][j] = human_avc[visit[i][j]]
print(res)