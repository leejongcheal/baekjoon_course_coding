from collections import deque, defaultdict

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = int(1e10)
M, N = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[INF] * M for _ in range(N)]
visit_d = defaultdict(list)
start = end = -1
for i in range(N):
    for j in range(M):
        if Map[i][j] == "C":
            if start == -1:
                start = (i, j)
            else:
                end = (i, j)
q = deque()
x, y = start
visit[x][y] = 0
visit_d[(x, y)] = [0, 1, 2, 3]
for d in range(4):
    q.append((x, y, d, 0))

while q:
    x, y, d, cnt = q.popleft()
    if (x, y) == end:
        res = cnt
        break
    for nd, (dx, dy) in enumerate(steps):
        nx, ny = x + dx, y + dy
        next_cnt = cnt + 1
        if nd == d:
            next_cnt = cnt
        # 없어도 문제는 풀림 밑에서 조건이 걸리기 때문에
        # -> 그래도 의도적으로 사용 + 시간조금이라도 빨라질테니
        elif nd % 4 == (d + 2) % 4:
            continue
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "*":
            if visit[nx][ny] > next_cnt:
                visit[nx][ny] = next_cnt
                visit_d[(nx, ny)] = [nd]
            elif visit[nx][ny] == next_cnt and nd not in visit_d[(nx, ny)]:
                visit_d[(nx, ny)].append(nd)
            else:
                continue
            if next_cnt == cnt:
                q.appendleft((nx, ny, nd, cnt))
            else:
                q.append((nx, ny, nd, next_cnt))
print(cnt)