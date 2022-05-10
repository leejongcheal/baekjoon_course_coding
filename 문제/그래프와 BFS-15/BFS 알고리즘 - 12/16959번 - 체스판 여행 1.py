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
q.append((1, sx, sy, 0, 1))
q.append((1, sx, sy, 1, 1))
q.append((1, sx, sy, 2, 1))
res = -1
visit = defaultdict(int) # 번호 좌표 타입 = dist
visit[(1, sx, sy, 0)] = 1
visit[(1, sx, sy, 1)] = 1
visit[(1, sx, sy, 2)] = 1
temp1 = []
temp2 = []
while q:
    while q:
        num, x, y, type, dist = q.pop()
        if visit[(num, x, y, type)] < dist:
            continue
        if Map[x][y] == num + 1:
            num += 1
            if num == N*N:
                res = dist - 1
                break
            visit[(num,x ,y, type)] = dist
        # 나이트 이동
        if type == 0:
            nd = dist + 1
        else:
            nd = dist + 2
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[(num,nx,ny,0)] == 0 or visit[(num, nx, ny, 0)] > nd:
                visit[(num, nx, ny, 0)] = nd
                if type == 0:
                    temp1.append((num, nx, ny, 0, nd))
                else:
                    temp2.append((num, nx, ny, 0, nd))
        # 비숍 룩 이동
        for ntype, oper in [(1, bishop), (2, lock)]:
            if ntype == type:
                nd = dist + 1
            else:
                nd = dist + 2
            for dx, dy in oper:
                nx, ny = x, y
                while 0 <= nx + dx < N and 0 <= ny + dy < N:
                    nx += dx
                    ny += dy
                    if visit[(num, nx,ny,ntype)] == 0 or visit[(num, nx,ny,ntype)] > nd:
                        visit[(num, nx,ny,ntype)] = nd
                        if type == ntype:
                            temp1.append((num, nx, ny, ntype, nd))
                        else:
                            temp2.append((num, nx, ny, ntype, nd))
    if res != -1:
        break
    q = temp1
    temp1 = temp2
    temp2 = []
print(res)




