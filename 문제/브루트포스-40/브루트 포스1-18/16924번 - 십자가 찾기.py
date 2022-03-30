steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def check(x, y):
    global star_cnt
    size = 0
    r_flag = 0
    for i in range(1, N):
        flag = 0
        change = set()
        for dx, dy in steps:
            nx, ny = x + dx*i, y + dy*i
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != ".":
                if Map[nx][ny] == "*":
                    change.add((nx, ny))
            else:
                flag = 1
                break
        if flag:
            break
        size = i
        for cx, cy in change:
            Map[cx][cy] = "#"
            star_cnt -= 1
            r_flag = 1
    if r_flag:
        if Map[x][y] == "*":
            Map[x][y] = "#"
            star_cnt -= 1
        res.append([x + 1, y + 1, size])


N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
star_cnt = 0
res = []
for m in Map:
    star_cnt += m.count("*")
for i in range(N):
    for j in range(M):
        if Map[i][j] != ".":
            check(i, j)
if star_cnt != 0:
    print(-1)
else:
    print(len(res))
    for r in res:
        print(*r)
# for m in Map:
#     print(m)