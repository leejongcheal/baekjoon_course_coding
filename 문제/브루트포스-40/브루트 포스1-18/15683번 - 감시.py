from copy import deepcopy


def cctv1(x, y, d, L, blank_cnt):
    temp = deepcopy(L)
    dx, dy = steps[d]
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
        if temp[nx][ny] == 0:
            temp[nx][ny] = "#"
            blank_cnt -= 1
        nx += dx
        ny += dy
    return temp, blank_cnt



def cctv2(x, y, d1, d2, L, blank_cnt):
    temp = deepcopy(L)
    for d in [d1, d2]:
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
            if temp[nx][ny] == 0:
                temp[nx][ny] = "#"
                blank_cnt -= 1
            nx += dx
            ny += dy
    return temp, blank_cnt

def cctv3(x, y, d1, d2, L, blank_cnt):
    temp = deepcopy(L)
    for d in [d1, d2]:
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
            if temp[nx][ny] == 0:
                temp[nx][ny] = "#"
                blank_cnt -= 1
            nx += dx
            ny += dy
    return temp, blank_cnt

def cctv4(x, y, d1, d2, d3, L, blank_cnt):
    temp = deepcopy(L)
    for d in [d1, d2, d3]:
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
            if temp[nx][ny] == 0:
                temp[nx][ny] = "#"
                blank_cnt -= 1
            nx += dx
            ny += dy
    return temp, blank_cnt


def cctv5(x, y, L, blank_cnt):
    temp = deepcopy(L)
    for d in [0, 1, 2, 3]:
        dx, dy = steps[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
            if temp[nx][ny] == 0:
                temp[nx][ny] = "#"
                blank_cnt -= 1
            nx += dx
            ny += dy
    return temp, blank_cnt


def dfs(cctv_index, L, blank_cnt):
    global res
    # if blank_cnt > res:
    #     return
    if cctv_index == cnt_cctv:
        res = min(res, blank_cnt)
        return
    x, y, number = pos_cctv[cctv_index]
    if number == 1:
        for d in cctv[number - 1]:
            temp, blank = cctv1(x, y, d, L, blank_cnt)
            dfs(cctv_index + 1, temp, blank)
    elif number == 2:
        for d1, d2 in cctv[number - 1]:
            temp, blank = cctv2(x, y, d1, d2, L, blank_cnt)
            dfs(cctv_index + 1, temp, blank)
    elif number == 3:
        for d1, d2 in cctv[number - 1]:
            temp, blank = cctv3(x, y, d1, d2, L, blank_cnt)
            dfs(cctv_index + 1, temp, blank)
    elif number == 4:
        for d1, d2, d3 in cctv[number - 1]:
            temp, blank = cctv4(x, y, d1, d2, d3, L, blank_cnt)
            dfs(cctv_index + 1, temp, blank)
    elif number == 5:
        temp, blank = cctv5(x, y, L, blank_cnt)
        dfs(cctv_index + 1, temp, blank)


steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cctv = [[0, 1, 2, 3], [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)], [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
pos_cctv = []  # x , y ,index
cnt_blank = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            cnt_blank += 1
        elif 1 <= Map[i][j] <= 5:
            pos_cctv.append((i, j, Map[i][j]))
cnt_cctv = len(pos_cctv)
res = 1e10
dfs(0, Map, cnt_blank)
print(res)