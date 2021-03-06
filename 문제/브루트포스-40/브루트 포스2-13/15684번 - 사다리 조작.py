def check1(y):
    for x in range(0, N):
        if Map[x][y] != 0:
            if y - 1 >= 0 and Map[x][y - 1] == Map[x][y]:
                y -= 1
            elif y + 1 < M and Map[x][y + 1] == Map[x][y]:
                y += 1
    return y


def check():
    for i in range(M):
        if i != check1(i):
            return 0
    return 1


def dfs(pre_x, pre_y, cnt):
    global res
    if check():
        res = min(cnt, res)
        return
    if cnt + 1 >= res:
        return
    for x in range(N):
        for y in range(M - 1):
            if 10*x + y <= pre_x*10 + pre_y:
                continue
            if Map[x][y] == 0 and Map[x][y+1] == 0 and cnt + 1 < res:
                Map[x][y] = Map[x][y+1] = idx + cnt
                dfs(x, y, cnt + 1)
                Map[x][y] = Map[x][y + 1] = 0


M, K, N = map(int, input().split())
Map = [[0]*M for _ in range(N)]
idx = 1
for _ in range(K):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    Map[a][b] = Map[a][b+1] = idx
    idx += 1
res = 4
dfs(-1, -1, 0)
if res == 4:
    res = -1
print(res)

# 후에 복습할때 BFS로 최대한 이쁘게 풀어보니 9% 시간초과
# 흠... 그냥 돌아가는 순서가 에바인듯?
# 애초에 전수조사 하라고 만든 문제인데 BFS안돌아가면 문제에러 아니냐 이건 너무하네 진짜.
# 복습할떄 풀이는 맞게 40분컷냄. 근데 단지 BFS라는 이유로 틀림