from collections import defaultdict


# 이동및 이동한 체스들 값 업데이트
def white(x, y, nx, ny, index):
    global flag
    pos = q_Map[x][y].index(index)
    temp = q_Map[x][y][pos:]
    if q_Map[nx][ny] == 0:
        q_Map[nx][ny] = temp
    else:
        q_Map[nx][ny] += temp
    q_Map[x][y] = q_Map[x][y][:pos]
    if len(q_Map[x][y]) == 0:
        q_Map[x][y] = 0
    if len(q_Map[nx][ny]) >= 4:
        flag = 1
    for i in temp:
        chess[i][0], chess[i][1] = nx, ny


def red(x, y, nx, ny, index):
    global flag
    pos = q_Map[x][y].index(index)
    temp = q_Map[x][y][pos:]
    if q_Map[nx][ny] == 0:
        q_Map[nx][ny] = temp[::-1]
    else:
        q_Map[nx][ny] += temp[::-1]
    q_Map[x][y] = q_Map[x][y][:pos]
    if len(q_Map[x][y]) == 0:
        q_Map[x][y] = 0
    if len(q_Map[nx][ny]) >= 4:
        flag = 1
    for i in temp:
        chess[i][0], chess[i][1] = nx, ny


def blue(index):
    x, y, d = chess[index]
    d += 1
    if d == 2:
        d = 0
    elif d == 4:
        d = 2
    chess[index][2] = d
    dx, dy = steps[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        if Map[nx][ny] == 0:
            white(x, y, nx, ny, index)
        elif Map[nx][ny] == 1:
            red(x, y, nx, ny, index)
    # 범위밖 또는 파랑색을 만나는경우 반대방향 및 좌표 유지


steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오 왼 위 아래
flag = 0
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
q_Map = [[0] * N for _ in range(N)]
chess = defaultdict()
for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    chess[i] = [x - 1, y - 1, d - 1]
    q_Map[x - 1][y - 1] = [i]
# 맵과 체스 완성
time = 1
res = -1
while time <= 1000:
    for index in range(1, K + 1):
        x, y, d = chess[index]
        # 맨아래에 있는경우만 이동
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if Map[nx][ny] == 0:
                white(x, y, nx, ny, index)
            elif Map[nx][ny] == 1:
                red(x, y, nx, ny, index)
            elif Map[nx][ny] == 2:
                blue(index)
        else:
            blue(index)
        if flag:
            break
    if flag:
        res = time
        break
    time += 1
print(res)
