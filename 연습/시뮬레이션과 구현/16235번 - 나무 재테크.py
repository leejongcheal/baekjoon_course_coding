steps = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
N, M, K = map(int, input().split())
plus = [list(map(int, input().split())) for _ in range(N)]
tree = [list(map(int, input().split())) for _ in range(M)]
muck = [[5] * N for _ in range(N)]
Map = [[dict() for _ in range(N)] for _ in range(N)]  # [(old:cnt)....] 값을 가짐
for x, y, old in tree:
    if Map[x - 1][y - 1].get(old, 0) == 0:
        Map[x - 1][y - 1][old] = 1
    else:
        Map[x - 1][y - 1][old] += 1
time = 0
while time < K:
    # 봄
    death = [[0] * N for _ in range(N)]
    new_tree = [[0]*N for _ in range(N)]
    time += 1
    for i in range(N):
        for j in range(N):
            if not Map[i][j]:
                continue
            new = dict()
            for old in sorted(Map[i][j].keys()):
                if muck[i][j] >= old * Map[i][j][old]:
                    muck[i][j] -= old * Map[i][j][old]
                    new[old + 1] = Map[i][j][old]
                    if (old + 1) % 5 == 0:
                        new_tree[i][j] += Map[i][j][old]
                else:
                    r, c = divmod(muck[i][j], old)
                    if r:
                        new[old + 1] = r
                        if (old + 1) % 5 == 0:
                            new_tree[i][j] += r
                    muck[i][j] = c
                    death[i][j] += (Map[i][j][old] - r) * (old // 2)
            Map[i][j] = new
    # 여름
    for i in range(N):
        for j in range(N):
            muck[i][j] += death[i][j]
    # 가을
    for i in range(N):
        for j in range(N):
            if new_tree[i][j]:
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if Map[nx][ny].get(1, 0) == 0:
                            Map[nx][ny][1] = new_tree[i][j]
                        else:
                            Map[nx][ny][1] += new_tree[i][j]
    # 겨울
    for i in range(N):
        for j in range(N):
            muck[i][j] += plus[i][j]
res = 0
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            res += sum(Map[i][j].values())
print(res)