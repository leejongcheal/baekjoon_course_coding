from collections import deque
def solve():
    res = 1
    for i in range(N):
        for j in range(N):
            if Map[i][j] == "X":
                Map[i][j] = 0
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in steps:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == "X":
                            if res == 1:
                                res = 2
                            Map[nx][ny] = Map[x][y] ^ 1
                            q.append((nx, ny))
                        elif 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == Map[x][y]:
                            return 3
    return res

N = int(input())
steps = [(-1, 0),(-1, 1),(0,-1),(0,1),(1, -1),(1, 0)]
res = 0
Map = [list(input()) for _ in range(N)]
if sum([x.count("X") for x in Map]) == 0:
    res = 0
else:
    res = solve()
print(res)