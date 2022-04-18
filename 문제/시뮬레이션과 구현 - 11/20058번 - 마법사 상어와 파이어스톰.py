from collections import deque
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
def rotate(x, y, L):
    for i in range(2**L):
        for j in range(2**L):
            temp[x+j][y-i+2**L-1] = Map[x+i][y+j]
N, M = map(int, input().split())
N = 2 ** N
Map = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))
for L in L_list:
    temp = [[0]*N for _ in range(N)]
    x, y = 0, 0
    rotate(x, y, L)
    while x < N:
        y += 2**L
        if y < N:
            rotate(x, y, L)
        else:
            x += 2**L
            y = 0
            if x < N:
                rotate(x, y, L)

    # 확인 temp에 대해서
    Map = [x[::] for x in temp]
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 0:
                continue
            cnt = 0
            for dx, dy in steps:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] != 0:
                    cnt += 1
            if cnt < 3:
                temp[i][j] -= 1
    Map = temp
total = sum([sum(x) for x in Map])
max_chunk = 0
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0 and visit[i][j] == 0:
            visit[i][j] = 1
            now = 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] != 0 and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        now += 1
                        q.append((nx, ny))
            max_chunk = max(max_chunk, now)
print(total)
print(max_chunk)