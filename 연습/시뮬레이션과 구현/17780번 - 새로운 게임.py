from collections import defaultdict
def change_d(d):
    d += 1
    if d == 2:
        d = 0
    elif d == 4:
        d = 2
    return d

# 그곳으로 이동하면서
# 1, 비어있는곳으로 가는지
# 2. 내가 리스트인지 확인
# 3. 4개가 쌓아지는지 -> 수정된 nex 리스트들에 대해서 q_Map, chess 업데이트
def white(x, y, nx, ny, index):
    global flag, q_Map, chess
    d = chess[index][2]
    new = q_Map[x][y][::1]
    if q_Map[nx][ny] == 0:
        q_Map[nx][ny] = new
    elif q_Map[nx][ny] != 0:
        old = q_Map[nx][ny][::1]
        q_Map[nx][ny] = old + new
    q_Map[x][y] = 0
    for i in new:
        x, y, td = chess[i]
        chess[i] = [nx, ny, td]

    if len(q_Map[nx][ny]) >= 4:
        # print("end check")
        # for q in q_Map:
        #     print(q)
        flag = 1


def red(x, y, nx, ny, index):
    global flag, q_Map, chess
    d = chess[index][2]
    new = q_Map[x][y][::-1]
    if q_Map[nx][ny] == 0:
        q_Map[nx][ny] = new
    elif q_Map[nx][ny] != 0:
        old = q_Map[nx][ny][::1]
        q_Map[nx][ny] = old + new
    q_Map[x][y] = 0
    for i in new:
        x, y, td = chess[i]
        chess[i] = [nx, ny, td]
    if len(q_Map[nx][ny]) >= 4:
        # print("end check")
        # for q in q_Map:
        #     print(q)
        flag = 1


def blue(x, y, index):
    global flag, q_Map, chess
    d = chess[index][2]
    nd = change_d(d)
    chess[index] = [x, y, nd]
    dx, dy = steps[nd]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        if Map[nx][ny] == 0:
            white(x, y, nx, ny, index)
        elif Map[nx][ny] == 1:
            red(x, y, nx, ny, index)

    # 파랑 또는 넘어가는경우 방향만 바꺼주기




steps = [(0, 1),(0, -1),(-1, 0),(1, 0)]
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
q_Map = [[0]*N for _ in range(N)] # 0 or [(i, d), ... 위]
chess = defaultdict()
for i in range(K):
    x, y, d = map(int, input().split())
    chess[i + 1] = [x - 1, y - 1, d - 1]
    q_Map[x - 1][y - 1] = [i + 1]
time = 1
res = -1
flag = 0
while time <= 1000:
    # move 도중에 말이 4개 쌓이면 브레이크
    for index in range(1, K + 1):
        x, y, d = chess[index]
        # 해당번호가 이동가능한 경우
        if len(q_Map[x][y]) == 1 or (q_Map[x][y][0] == index):
            dx, dy = steps[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if Map[nx][ny] == 0:
                    white(x, y, nx, ny, index)
                elif Map[nx][ny] == 1:
                    red(x, y, nx, ny, index)
                elif Map[nx][ny] == 2:
                    blue(x, y, index)
            else:
                blue(x, y, index)
            if flag:
                break
    #     print(index, flag)
    #     for q in q_Map:
    #         print(q)
    #     print()
    # # print(time)
    # print(index, flag)
    if flag:
        res = time
        break
    time += 1
print(res)

