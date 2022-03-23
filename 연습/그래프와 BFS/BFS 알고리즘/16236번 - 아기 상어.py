from collections import deque

steps= [(1, 0),(0, 1),(-1, 0),(0, -1)]
INF = int(1e10)
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
fish_total = 0
for i in range(N):
    for j in range(N):
        if 0 < Map[i][j] <= 6:
            fish_total += 1
        elif Map[i][j] == 9:
            shark_x, shark_y = i, j
shark_size = 2
now_eat = 0
time = 0
while 1:
    # 가장가까운 먹을 물고기들
    eat_possible = []
    q = deque()
    visit = [[0]*N for _ in range(N)]
    q.append((0, shark_x, shark_y))
    visit[shark_x][shark_y] = 1
    min_dist = INF
    while q:
        dist, x, y = q.popleft()
        if dist > min_dist:
            break
        if 0 < Map[x][y] < shark_size and not (x == shark_x and y == shark_y):
            min_dist = dist
            eat_possible.append((x, y))
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N \
                and visit[nx][ny] == 0 and Map[nx][ny] <= shark_size:
                visit[nx][ny] = 1
                q.append((dist + 1, nx, ny))
    # 먹을수 있는 물고기가 없는경우
    if len(eat_possible) == 0:
        break
    else:
        eat_possible.sort()
        nx, ny = eat_possible[0]
        Map[nx][ny] = 9
        Map[shark_x][shark_y] = 0
        shark_x, shark_y = nx, ny
        now_eat += 1
        if now_eat == shark_size:
            shark_size += 1
            now_eat = 0
    time += min_dist
print(time)
# 상어 사이즈가 9보다 커지는 경우