from collections import deque
import sys
print = sys.stdin.readline
def check(now_lebber):
    for x in range(N):
        j = 0
        i = x
        while j < H:
            if Map[j][i] != 0:
                ch = [i+1, i-1]
                for next_i in ch:
                    if 0 <= next_i < N and Map[j][next_i] == Map[j][i]:
                        i = next_i
                        break
            j += 1
        if i != x:
            return 0
    return 1


def idx_check(sx, sy, x, y, now_lebber):
    if (x, y) > (sx, sy) and Map[x][y] == 0 and Map[x][y+1] == 0:
        return 1
    return 0

N, M, H = map(int, input().split())
Map = [[0]*N for _ in range(H)]
pre_lebber = []
for i in range(1, M+1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    Map[a][b] = Map[a][b+1] = i
    pre_lebber.append((a, b))
q = deque()
q.append([])
res = -1
while q:
    now_lebber = q.popleft()
    if len(now_lebber) > 3:
        break
    for idx, (x, y) in enumerate(now_lebber, 1):
        Map[x][y] = Map[x][y+1] = M+idx
    if check(now_lebber):
        res = len(now_lebber)
        break
    # cnt +1 해서 가능한 좌표들에 대해서 q 삽입
    if now_lebber:
        sx, sy = now_lebber[-1]
    else:
        sx, sy = -1, -1
    for x in range(H):
        for y in range(N-1):
            if idx_check(sx, sy, x, y, now_lebber):
                q.append(now_lebber + [(x, y)])
    # 맵 초기화
    for idx, (x, y) in enumerate(now_lebber, 1):
        Map[x][y] = Map[x][y+1] = 0
print(res)

