from collections import defaultdict


def change_d(d):
    d += 1
    if d == 2:
        d = 0
    elif d == 4:
        d = 2
    return d


steps = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 2 -> 0 4-> 2 위 아래 오른 왼
N, M, S = map(int, input().split())
Map = defaultdict(list)
for _ in range(S):
    x, y, s, d, z = map(int, input().split())
    d -= 1
    if d < 2:
        s %= (N-1)*2
    else:
        s %= (M-1)*2
    Map[(x - 1, y - 1)].append((z, s, d))
# 상어 위치 넣기
index = 0
res = 0
# print(Map)
while index < M:
    # 상어잡기 + 상어이동도 동시에하기
    min_x = N
    for x, y in Map.keys():
        if y == index:
            min_x = min(min_x, x)
    if min_x != N:
        res += Map[(min_x, index)][0][0]
    # 상어 이동 -> 겹치는 상어 없애기
    temp = defaultdict(list)
    for x, y in Map.keys():
        if x == min_x and y == index:
            continue
        z, s, d = Map[(x, y)][0]
        nx, ny = x, y
        for _ in range(s):
            dx, dy = steps[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                d = change_d(d)
                dx, dy = steps[d]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
        temp[(x, y)].append((z, s, d))
    for key in temp.keys():
        if len(temp[key]) > 1:
            temp[key].sort()
            temp[key] = [temp[key][-1]]
    Map = temp
    # print(Map)
    index += 1
print(res)
