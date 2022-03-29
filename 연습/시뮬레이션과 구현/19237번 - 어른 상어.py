from collections import defaultdict

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
shark = defaultdict(list)  # 요소 인덱스 현재방향
L = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            index = Map[i][j]
            Map[i][j] = [index - 1, K]
            shark[(i, j)].append((index - 1, L[index - 1] - 1))
direction = []
for shark_index in range(1, M + 1):
    shark_direction = []
    for d in range(4):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        shark_direction.append([a, b, c, d])
    direction.append(shark_direction)
time = 1
res = - 1
while time <= 1000:
    # 상어들이 이동할 좌표 및 방향 구하기
    temp_shark = defaultdict(list)
    for x,y in shark.keys():
        index, d = shark[(x, y)][0]
        now_steps = direction[index][d]
        res_x, res_y, res_d = -1, -1, -1
        # for dx, dy in now_steps:
        # 빈자리 먼저 구하기
        for nd in now_steps:
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == 0:
                res_x, res_y, res_d = nx, ny, nd
                break
        # 빈자리 못구했으면 내냄새로
        if res_x == -1:
            for nd in now_steps:
                dx, dy = steps[nd]
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] != 0 and Map[nx][ny][0] == index:
                    res_x, res_y, res_d = nx, ny, nd
                    break
        temp_shark[(res_x, res_y)].append([index, res_d])
    # k -= 1 해주고
    for i in range(N):
        for j in range(N):
            if Map[i][j] != 0:
                Map[i][j][1]-= 1
                if Map[i][j][1] == 0:
                    Map[i][j] = 0
    # 상어 채워주면서 겹치는 상어 삭제해서 새로운 shark 만들기
    shark = defaultdict(list)
    for x, y in temp_shark.keys():
        temp_shark[(x, y)].sort()
        index, d = temp_shark[(x, y)][0]
        shark[(x, y)].append([index, d])
        Map[x][y] = [index, K]
    # shark를 통해 0만남으면 res = time후 break
    if len(shark.keys()) == 1:
        res = time
        break
    time += 1
print(res)