# 1111 남동북서
from collections import deque


def bfs(x, y, index):
    size = 1
    q = deque()
    visit[x][y] = index
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            # 해당 방향이 뚫려 있다 -> 0값가짐
            if Map[x][y][i] == 0:
                dx, dy = steps[i]
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1:
                    visit[nx][ny] = index
                    size += 1
                    q.append((nx, ny))
    return size


steps = [(0 ,-1),(-1, 0),(0, 1),(1, 0)]
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
# 원소값 [1,1,1,1] 서 북 동 남 순서를 뜻함
for i in range(N):
    for j in range(M):
        bit = bin(Map[i][j])[2:]
        temp = [0]*4
        for b in range(len(bit)):
            if bit[-1-b] == "1":
                temp[b] = 1
        Map[i][j] = temp


visit = [[-1]*M for _ in range(N)] # 방번호겸 방문체크
room_index_size = []
room_cnt = 0
max_room = 0
max_2room = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == -1:
            room_index_size.append(bfs(i,j, room_cnt))
            room_cnt += 1
max_room = max(room_index_size)
for x in range(N):
    for y in range(M):
        for dx, dy in [(1, 0),(0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[x][y] != visit[nx][ny]:
                a = room_index_size[visit[x][y]]
                b = room_index_size[visit[nx][ny]]
                max_2room = max(max_2room, a + b)
print(room_cnt)
print(max_room)
print(max_2room)

