from collections import deque, defaultdict
visit = defaultdict(int) # 도달한 갯수를 저장하자.
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
shape = 0 # - 0 | 1 \ 2 로 두자
x, y = 0, 1
visit[(x, y, shape)] = 1
q = deque()
q.append((x, y, shape))
while q:
    x, y, shape = q.popleft()
    # -> 이동
    if shape in [0, 2]:
        nx, ny = x , y + 1
        if 0 <= ny < N and Map[nx][ny] == 0:
            if visit[(nx, ny, 0)] == 0:
                q.append((nx, ny, 0))
            visit[(nx, ny, 0)] += visit[(x, y, shape)]
    # | 이동
    if shape in [1, 2]:
        nx, ny = x + 1, y
        if 0 <= nx < N and Map[nx][ny] == 0:
            if visit[(nx, ny, 1)] == 0:
                q.append((nx, ny, 1))
            visit[(nx, ny, 1)] += visit[(x, y, shape)]
    # \ 이동
    nx, ny = x + 1, y + 1
    if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == Map[x][y+1] == Map[x+1][y] == 0:
        if visit[(nx, ny, 2)] == 0:
            q.append((nx, ny, 2))
        visit[(nx, ny, 2)] += visit[(x, y, shape)]
res = visit[(N-1, N-1, 0)] + visit[(N-1, N-1, 1)] + visit[(N-1, N-1, 2)]
print(res)