from collections import deque
width_steps = [((0, 1, 0),(0, 1, 0)),((0,1, 0),(1, 1, 1))]
height_steps = [((1,0, 0),(1,0, 0)),((1,0, 0),(1,1,1))]
diagonal_steps = [((1,1 ,1),(0,1,0)),((1,1,1),(1,0,0)),((1,1,1),(1,1,1))]

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
pipe = [(0, 0), (0, 1)]
res = 0
q = deque()
q.append((0, 0, 0, 1, 0))
while q:
    x1, y1, x2, y2, d = q.popleft()
    if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
        res += 1
        continue
    # 가로
    now_steps = []
    if x1 == x2 and y1 != y2:
        now_steps = width_steps
    # 세로
    elif x1 != x2 and y1 == y2:
        now_steps = height_steps
    # 대각선
    else:
        now_steps = diagonal_steps
    # 다음 n1 n2들이 벽이 아니거나 범위를 만족한다면 q에 넣어주기
    for step1, step2 in now_steps:
        dx1, dy1, f1 = step1
        dx2, dy2, f2 = step2
        nx1, ny1 = x1 + dx1, y1 + dy1
        nx2, ny2 = x2 + dx2, y2 + dy2
        if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N\
            and Map[nx1][ny1] != 1 and Map[nx2][ny2] != 1:
            if f1 and (Map[x1 + 1][y1] == 1 or Map[x1][y1 + 1] == 1):
                continue
            if f2 and (Map[x2 + 1][y2] == 1 or Map[x2][y2 + 1] == 1):
                continue
            q.append((nx1, ny1, nx2, ny2, d + 1))
print(res)

