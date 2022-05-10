from collections import deque, defaultdict
knight = [(-2, -1),(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2),(-1, -2)]
bishop = [(-1, -1),(-1, 1),(1, 1),(1, -1)]
lock = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            sx, sy = i, j
q = deque()
q.append((1, sx, sy, 0, 1, 0)) # type, dist, change 순
q.append((1, sx, sy, 1, 1, 0))
q.append((1, sx, sy, 2, 1, 0))
INF = int(1e10)
res = [INF,INF]
visit = defaultdict(int) # 번호 좌표 타입 = dist
visit[(1, sx, sy, 0)] = [1, 0]
visit[(1, sx, sy, 1)] = [1, 0]
visit[(1, sx, sy, 2)] = [1, 0]
temp1 = []
temp2 = []
while q:
    while q:
        num, x, y, type, dist, change = q.pop()
        if visit[(num, x, y, type)] < [dist, change]:
            continue
        if Map[x][y] == num + 1:
            num += 1
            if num == N*N:
                if res > [dist-1, change]:
                    res = [dist-1, change]
            visit[(num,x ,y, type)] = [dist, change]
        # 나이트 이동
        if type == 0:
            nd = [dist + 1, change]
        else:
            nd = [dist + 2, change+1]
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (visit[(num,nx,ny,0)] == 0 or visit[(num, nx, ny, 0)] > nd):
                visit[(num, nx, ny, 0)] = nd
                if type == 0:
                    temp1.append((num, nx, ny, 0, nd[0], nd[1]))
                else:
                    temp2.append((num, nx, ny, 0, nd[0], nd[1]))
        # 비숍 룩 이동
        for ntype, oper in [(1, bishop), (2, lock)]:
            if ntype == type:
                nd = [dist + 1, change]
            else:
                nd = [dist + 2, change + 1]
            for dx, dy in oper:
                nx, ny = x, y
                while 0 <= nx + dx < N and 0 <= ny + dy < N:
                    nx += dx
                    ny += dy
                    if visit[(num, nx,ny,ntype)] == 0 or visit[(num, nx,ny,ntype)] > nd:
                        visit[(num, nx,ny,ntype)] = nd
                        if type == ntype:
                            temp1.append((num, nx, ny, ntype, nd[0],nd[1]))
                        else:
                            temp2.append((num, nx, ny, ntype, nd[0], nd[1]))
    if res[0] != INF:
        break
    q = temp1
    temp1 = temp2
    temp2 = []
print(res[0], res[1])




