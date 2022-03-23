from collections import deque, defaultdict

steps = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
Map = [list(input()) for _ in range(8)]
sx, sy, ex, ey = 7, 0, 0, 7
blank_index = []
for i in range(8):
    for j in range(8):
        if Map[i][j] == "#":
            blank_index.append((i, j))
time = 0
blank = defaultdict(set)
while blank_index:
    next = []
    for x, y in blank_index:
        blank[(x, y)].add(time)
        if x < 7:
            x += 1
            next.append((x, y))
    blank_index = next
    time += 1
flag = 0
q = deque()
visit = defaultdict(set)  # (x, y)에 time있으면 방문했다는 뜻 그시간 그자리
# x, y , cnt
q.append((7, 0, 0))
visit[(7, 0)].add(0)
while q:
    x, y, cnt = q.popleft()
    # 벽에 갇히는 경우
    if cnt in blank[(x, y)]:
        continue
    # 갯수가 7개 이상인데 현재 살아있는경우 -> 벽은 이미 맨아래 남아 있으며 벽에 갇히지 않는경우니 무조건 어디로든 갈수있음
    if cnt >= 7:
        flag = 1
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            # 지금 벽이라서 이동못하는 경우
            if cnt in blank[(nx, ny)]:
                continue
            # 이미 큐에 있거나 방문한적없는 x,y,cnt 경우일때, q에 넣어줌
            if cnt + 1 not in visit[(nx, ny)]:
                visit[(nx, ny)].add(cnt + 1)
                q.append((nx, ny, cnt + 1))
print(flag)