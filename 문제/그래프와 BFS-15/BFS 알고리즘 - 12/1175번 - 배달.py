from collections import deque, defaultdict
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
C_list = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == "C":
            C_list.append((i, j))
        if Map[i][j] == "S":
            sx, sy = i, j
visit = [set() for _ in range(3)]
res = -1
q = deque() # t, visit 0 1 2, pred, x, y
q.append((0, 0, -1, sx, sy))
for i in range(4):
    visit[0].add((i, sx, sy))
while q:
    t, num, pred, x, y = q.popleft()
    if num == 0 and (x, y) in C_list:
        num = 1 + C_list.index((x, y))
        visit[num].add((d, x, y))
    # 2번 방문하는 경우
    elif num != 0 and (x, y) == C_list[num%2]:
        res = t
        break
    for d, (dx, dy) in  enumerate(steps):
        if d == pred:
            continue
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "#" and (d, nx, ny) not in visit[num]:
            visit[num].add((d, nx, ny))
            q.append((t+1, num, d, nx, ny))
print(res)


