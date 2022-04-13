from collections import deque


def BFS(num: int):
    q = deque()
    max_dist = D[num - 1]
    next_pos = set()
    flag = 0
    for x, y in pos[num]:
        q.append((x, y, 0))
    while q:
        x, y, now_dist = q.popleft()
        if now_dist >= max_dist:
            break
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == ".":
                Map[nx][ny] = str(num)
                q.append((nx, ny, now_dist + 1))
                next_pos.add((nx, ny))
                flag = 1
    pos[num] = next_pos
    return flag


steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M, P = map(int, input().split())
D = list(map(int, input().split()))
Map = [list(input()) for _ in range(N)]
remember = [i for i in range(1, P + 1)]
pos = [set() for _ in range(P + 1)]
for i in range(N):
    for j in range(M):
        if Map[i][j] not in [".", "#"]:
            pos[int(Map[i][j])].add((i, j))
while remember:
    temp = []
    for i in remember:
        if BFS(i):
            temp.append(i)
    remember = temp
cnt = [0]*P
for i in range(N):
    for j in range(M):
        if Map[i][j] not in [".", "#"]:
            cnt[int(Map[i][j]) - 1] += 1
print(*cnt)
