from collections import deque, defaultdict

knight = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
bishop = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
lock = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
INF = int(1e10)
Map = [list(map(int, input().split())) for _ in range(N)]
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# graph [나이트 비숍 룩 0  1 2] [해당값에서][해당값으로이동]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            sx, sy = i, j
# q = 현재번호(1시작 N^N이면 끝) x y 말타입(0,1,2 나이트 비숍 룩) 거리 말 바꾼 횟수
q = deque()
q.append((1, sx, sy, 0, 0, 0))
q.append((1, sx, sy, 1, 0, 0))
q.append((1, sx, sy, 2, 0, 0))
res = []
visit = defaultdict(int)  # [번호,좌표,타입] 를 key로 가지고 원소를 [작은dist, 작은 말바꾼 횟수]
visit[(1, sx, sy, 0)] = 0
visit[(1, sx, sy, 1)] = 0
visit[(1, sx, sy, 2)] = 0
temp1 = []
temp2 = []
while q:
    temp2 = []
    while q:
        num, x, y, type, dist, change = q.pop()
        if Map[x][y] == num + 1:
            num += 1
            if num == N * N:
                res.append((change, dist))
                continue
            visit[(num, x, y, type)] = [dist, change]
        # 나이트 이동 0
        if type == 0:
            nd = dist
            nc = change
        else:
            nd = dist + 1
            nc = change + 1
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visit[(num, nx, ny, 0)] == 0 or visit[(num, nx, ny, 0)][0] > nd + 1 \
                        or (visit[(num, nx, ny, 0)][0] == nd + 1 and visit[(num, nx, ny, 0)][1] > nc):
                    visit[(num, nx, ny, 0)] = [nd + 1, nc]
                    if nd == dist:
                        temp1.append((num, nx, ny, 0, nd + 1, nc))
                    else:
                        temp2.append((num, nx, ny, 0, nd + 1, nc))
        # 비숍 이동 1
        if type == 1:
            nd = dist
            nc = change
        else:
            nd = dist + 1
            nc = change + 1
        for dx, dy in bishop:
            nx, ny = x + dx, y + dy
            while 0 <= nx < N and 0 <= ny < N:
                # if visit[(num, nx, ny, 1, nc)] == 0 or visit[(num, nx, ny, 1, nc)] > nd + 1:
                #    visit[(num, nx, ny, 1, nc)] = nd + 1
                if visit[(num, nx, ny, 1)] == 0 or visit[(num, nx, ny, 1)][0] > nd + 1 \
                        or (visit[(num, nx, ny, 1)][0] == nd + 1 and visit[(num, nx, ny, 1)][1] > nc):
                    visit[(num, nx, ny, 1)] = [nd + 1, nc]
                    if nd == dist:
                        temp1.append((num, nx, ny, 1, nd + 1, nc))
                    else:
                        temp2.append((num, nx, ny, 1, nd + 1, nc))
                nx += dx
                ny += dy
        # 룩이동  2
        if type == 2:
            nd = dist
            nc = change
        else:
            nd = dist + 1
            nc = change + 1
        for dx, dy in lock:
            nx, ny = x + dx, y + dy
            while 0 <= nx < N and 0 <= ny < N:
                # if visit[(num, nx, ny, 2, nc)] == 0 or visit[(num, nx, ny, 2, nc)] > nd + 1:
                #     visit[(num, nx, ny, 2, nc)] = nd + 1
                if visit[(num, nx, ny, 2)] == 0 or visit[(num, nx, ny, 2)][0] > nd + 1 \
                        or (visit[(num, nx, ny, 2)][0] == nd + 1 and visit[(num, nx, ny, 2)][1] > nc):
                    visit[(num, nx, ny, 2)] = [nd + 1, nc]
                    if nd == dist:
                        temp1.append((num, nx, ny, 2, nd + 1, nc))
                    else:
                        temp2.append((num, nx, ny, 2, nd + 1, nc))
                nx += dx
                ny += dy
    q = temp1
    temp1 = temp2
    if len(res) != 0:
        break
res.sort()
print(res[0][1], res[0][0])
