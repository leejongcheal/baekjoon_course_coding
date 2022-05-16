from collections import deque
def get_max(Map):
    Max = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] != "#":
                Max = max(Max, Map[i][j])
    return Max
def move(x, y, dx, dy, combine_idx):
    pass
def move_left(L):
    pass
def move_right(L):
    pass
def move_up(L):
    pass
def move_down(L):
    pass
# 위 아래 왼 오 각각의 이동함수 만들기
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append((Map, 0))
res = 0
while q:
    Map, cnt = q.popleft()
    if cnt == 5:
       res = max(res, get_max(Map))
       continue
    temp = [m[::] for m in Map]
    temp = move_left(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    temp = move_right(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    temp = move_up(temp)
    q.append((temp, cnt + 1))
    temp = [m[::] for m in Map]
    temp = move_down(temp)
    q.append((temp, cnt + 1))
print(res)







