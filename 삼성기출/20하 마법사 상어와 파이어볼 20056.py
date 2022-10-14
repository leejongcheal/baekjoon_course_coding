def move():
    global Map, steps, N
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(Map[i][j]) == 0:
                continue
            for m, s, d in Map[i][j]:
                dx, dy = steps[d]
                nx, ny = (i + dx * s) % N, (j + dy * s) % N
                temp[nx][ny].append([m, s, d])
    Map = temp


def split():
    global Map, steps, N
    cand = [(1, 3, 5, 7), (0, 2, 4, 6)]
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(Map[i][j]) == 0:
                continue
            elif len(Map[i][j]) == 1:
                temp[i][j] = Map[i][j][:]
                continue
            tm, ts, flag = 0, 0, 1
            check_d = Map[i][j][0][2] % 2
            for m, s, d in Map[i][j]:
                tm += m
                ts += s
                if d % 2 != check_d:
                    flag = 0
            m = tm // 5
            if m == 0:
                continue
            s = ts // len(Map[i][j])
            ds = cand[flag]
            for c in range(4):
                temp[i][j].append([m, s, ds[c]])
    Map = temp


N, M, K = map(int, input().split())
Map = [[[] for _ in range(N)] for _ in range(N)]
steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for cnt in range(M):
    i, j, m, s, d = map(int, input().split())
    Map[i - 1][j - 1].append([m, s, d])
for cnt in range(K):
    # 파이어볼 이동
    move()
    # 겹쳐진 파이어볼 처리
    split()
res = 0
for i in range(N):
    for j in range(N):
        for m, d, s in Map[i][j]:
            res += m
print(res)
