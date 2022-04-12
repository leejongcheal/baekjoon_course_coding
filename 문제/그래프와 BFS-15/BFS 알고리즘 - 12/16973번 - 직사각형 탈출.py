def up_move(x, y):
    if x == 0:
        return 0
    for j in range(W):
        if Map[x - 1][y + j] == 1:
            return 0
    return 1


def down_move(x, y):
    if x + H >= N:
        return 0
    for j in range(W):
        if Map[x + H][y + j] == 1:
            return 0
    return 1


def left_move(x, y):
    if y == 0:
        return 0
    for i in range(H):
        if Map[x + i][y - 1] == 1:
            return 0
    return 1


def right_move(x, y):
    if y + W >= M:
        return 0
    for i in range(H):
        if Map[x + i][y + W] == 1:
            return 0
    return 1


from collections import deque

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
H, W, sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
res = -1
visit = set()
visit.add((sx, sy))
q = deque()
q.append((0, sx, sy))
while q:
    time, x, y = q.popleft()
    if x == ex and y == ey:
        res = time
        break
    if up_move(x, y) and (x - 1, y) not in visit:
        visit.add((x - 1, y))
        q.append((time + 1, x - 1, y))
    if down_move(x, y) and (x + 1, y) not in visit:
        visit.add((x + 1, y))
        q.append((time + 1, x + 1, y))
    if left_move(x, y) and (x, y - 1) not in visit:
        visit.add((x, y - 1))
        q.append((time + 1, x, y - 1))
    if right_move(x, y) and (x, y + 1) not in visit:
        visit.add((x, y + 1))
        q.append((time + 1, x, y + 1))
print(res)
