def check(Map):
    flag = 1
    for j in range(M):
        x, y = 0, j
        while x < N:
            if Map[x][y] != 0:
                if y+1 < M and Map[x][y+1] == Map[x][y]:
                    x, y = x + 1, y + 1
                elif y - 1 >= 0 and Map[x][y-1] == Map[x][y]:
                    x, y = x + 1, y - 1
            elif Map[x][y] == 0:
                x, y = x + 1, y
        if y != j:
            return 0
    return 1


def dfs(Map, now, x, y):
    global res, line_cnt
    # 최솟값을 찾아야되는데 이미 2를 찾았으면 2,3조사가 아닌 1에 대해서만 조사하면됨.
    if res <= now:
        return
    if check(Map):
        res = min(res, now)
        return
    if now >= 3:
        return
    for i in range(N):
        for j in range(M-1):
            if i*10+j <= 10*x + y:
                continue
            # 전의 값보다 i,j 가 앞에 있는 경우
            if Map[i][j] == Map[i][j+1] == 0:
                Map[i][j] = Map[i][j+1] = 1 + line_cnt + now
                dfs(Map, now + 1, i, j + 1)
                Map[i][j] = Map[i][j+1] = 0


M, line_cnt, N = map(int, input().split())
Map = [[0]*M for _ in range(N)]
for i in range(line_cnt):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Map[a][b] = Map[a][b+1] = i + 1
INF = int(1e10)
res = INF
### 0,0 시작했는데 if i*10+j <= 10*x + y: 이부분 걸리는걸 생각못함..
dfs(Map, 0, -1, -1)
if res != INF:
    print(res)
else:
    print(-1)