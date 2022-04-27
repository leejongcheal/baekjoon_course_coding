from collections import defaultdict
def change_d(d):
    if d in [0,1]:
        d = d ^ 1
    else:
        d = (d-2)^1 + 2
    return d
def move(cnt, num):
    global flag
    x, y, d = horse_pos[num]
    dx, dy = steps[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        if Map[nx][ny] == 0 or Map[nx][ny] == 1:
            for i in horse_shape[(x, y)]:
                hx, hy, hd = horse_pos[i]
                horse_pos[i] = [nx, ny, hd]
            if Map[nx][ny] == 0:
                horse_shape[(nx, ny)].extend(horse_shape[(x, y)])
            elif Map[nx][ny] == 1:
                horse_shape[(nx, ny)].extend(horse_shape[(x, y)][::-1])
            if len(horse_shape[(nx, ny)]) >= 4:
                flag = 1
                return
            horse_shape[(x, y)] = []
        elif Map[nx][ny] == 2:
            if cnt == 0:
                d = change_d(d)
                horse_pos[num] = [x, y, d]
                move(cnt + 1, num)
    else:
        if cnt == 0:
            d = change_d(d)
            horse_pos[num] = [x, y, d]
            move(cnt + 1, num)



steps = [(0,1),(0,-1),(-1,0),(1, 0)]
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
horse_pos = []
horse_shape = defaultdict(list)
for i in range(K):
    x, y, d = map(int, input().split())
    x, y, d = x - 1, y - 1, d - 1
    horse_pos.append([x, y, d])
    horse_shape[(x, y)].append(i)
time = 1
flag = 0
while time <= 1000:
    # 말이동
    for i in range(K):
        x, y, d = horse_pos[i]
        # 이동 가능한 경우
        if horse_shape[(x, y)][0] == i:
            move(0, i)
    if flag == 1:
        break
    time += 1
if time > 1000:
    time = -1
print(time)