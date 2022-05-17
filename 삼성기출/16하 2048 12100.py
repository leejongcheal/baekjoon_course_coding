from collections import deque
def get_max(Map):
    Max = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] != "#":
                Max = max(Max, Map[i][j])
    return Max
def move(L, sx, sy, dx, dy, combine_idx):
    x, y = sx, sy
    if not (0 <= x + dx < N and 0 <= y + dy < N) or (L[x+dx][y+dy] != "#" and L[x+dx][y+dy] != L[sx][sy]):
        return
    while 0 <= x + dx < N and 0 <= y + dy < N:
        if L[x+dx][y+dy] == L[sx][sy]:
            if (x+dx, y + dy) not in combine_idx:
                combine_idx.append((x+dx, y + dy))
                L[x+dx][y+dy] *= 2
            else:
                L[x][y] = L[sx][sy]
            L[sx][sy] = "#"
            return
        elif L[x+dx][y+dy] != "#" and L[x+dx][y+dy] != L[sx][sy]:
            L[x][y] = L[sx][sy]
            L[sx][sy] = "#"
            return
        x += dx
        y += dy
    L[x][y] = L[sx][sy]
    L[sx][sy] = "#"
    return



def move_left(L):
    combine_idx = []
    for j in range(N):
        for i in range(N):
            if L[i][j] != "#":
                move(L, i, j, 0, -1, combine_idx)
def move_right(L):
    combine_idx = []
    for j in range(N-1, -1, -1):
        for i in range(N):
            if L[i][j] != "#":
                move(L, i, j, 0, 1, combine_idx)
def move_up(L):
    combine_idx = []
    for i in range(N):
        for j in range(N):
            if L[i][j] != "#":
                move(L, i, j, -1, 0, combine_idx)
def move_down(L):
    combine_idx = []
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if L[i][j] != "#":
                move(L, i, j, 1, 0, combine_idx)
# 위 아래 왼 오 각각의 이동함수 만들기
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 0:
            Map[i][j]= "#"
q = deque()
q.append((Map, 0))
res = 0
while q:
    Map, cnt = q.popleft()
    if cnt == 5:
       res = max(res, get_max(Map))
       continue
    temp = [m[::] for m in Map]
    move_left(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    move_right(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    move_up(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    move_down(temp)
    q.append((temp, cnt + 1))
print(res)