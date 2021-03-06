from collections import deque

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# o: 동전
# .: 빈 칸
# #: 벽
def bfs(x1, y1, x2, y2):
    visit = set()
    q = deque()
    visit.add((x1, y1, x2, y2))
    q.append((0, x1, y1, x2, y2))
    while q:
        cnt, x1, y1, x2, y2 = q.popleft()
        if cnt > 9:
            return -1
        for dx, dy in steps:
            nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
            if (not (0 <= nx1 < N) or not (0 <= ny1 < M)) and (0 <= nx2 < N and 0 <= ny2 < M):
                # print(1, cnt, nx1, ny1, nx2, ny2, x1, y1, x2, y2)
                return cnt + 1
            elif (not (0 <= nx2 < N) or not (0 <= ny2 < M)) and (0 <= nx1 < N and 0 <= ny1 < M):
                # print(2, cnt, nx1, ny1, nx2, ny2)
                return cnt + 1
            elif 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if L[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if L[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                if (nx1, ny1, nx2, ny2) not in visit:
                    q.append((cnt+1, nx1, ny1, nx2, ny2))
                    visit.add((nx1, ny1, nx2, ny2))
            else:
                continue
    return -1
N, M = map(int, input().split())
res = 0
x1 = y1 = x2 = y2 = -1
L = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if L[i][j] == "o":
            if x1 == -1:
                x1, y1 = i, j
            elif x2 == -1:
                x2, y2 = i, j
res = bfs(x1, y1, x2, y2)
print(res)
