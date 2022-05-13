steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
def rotate(x, y, M):
    for i in range(M):
        for j in range(M):
            temp[x+j][y+M-i-1] = Map[x+i][y+j]


def bfs(x, y):
    global max_cnt
    q = []
    cnt = 1
    q.append((x, y))
    while q:
        x, y = q.pop()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] > 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    max_cnt = max(max_cnt, cnt)

N, Q = map(int, input().split())
N = 2**N
Map = [list(map(int, input().split())) for _ in range(N)]
L = list(map(int, input().split()))
for l in L:
    M = 2**l
    start = [(0, 0)]
    x, y = 0, 0
    while 1:
        y += M
        if y >= N:
            x += M
            y = 0
        if x >= N:
            break
        start.append((x, y))
    # 회전
    temp = [[0] * N for _ in range(N)]
    for x, y in start:
        rotate(x, y, M)
    Map = temp
    # 얼음 녹이기
    original = [m[::] for m in Map]
    for i in range(N):
        for j in range(N):
            if original[i][j] != 0:
                cnt = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N and original[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    Map[i][j] -= 1
total = sum([sum(m) for m in Map])
visit = [[0]*N for _ in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0 and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i,j)
print(total)
print(max_cnt)