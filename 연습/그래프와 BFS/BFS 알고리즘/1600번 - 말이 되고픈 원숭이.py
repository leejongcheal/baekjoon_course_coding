from collections import deque, defaultdict

steps2 = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
steps = [(1,0),(-1,0),(0,1),(0,-1)]
visit = defaultdict(int)  # x, y ,K 에 대한 최소거리
K = int(input())
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append((0, 0, K, 0))  # x, y, 남은K, dist // dist오름차순으로 집어넣기
visit = [[[0]*M for _ in range(N)] for _ in range(K+1)]
visit[K][0][0] = 1
res = -1
while q:
    x, y, k, dist = q.popleft()
    if x == N - 1 and y == M - 1:
        res = dist
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0 and visit[k][nx][ny] == 0:
            visit[k][nx][ny] = 1
            q.append((nx, ny, k, dist + 1))
        if k:
            for dx, dy in steps2:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0 and visit[k -1][nx][ny] == 0:
                    visit[k - 1][nx][ny] = 1
                    q.append((nx, ny, k - 1, dist + 1))
print(res)