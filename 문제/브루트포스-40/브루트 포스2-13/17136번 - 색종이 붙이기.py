def check_t(Map, x, y, t):
    if x + t > 10 or y + t > 10:
        return 0
    for i in range(t):
        for j in range(t):
            if Map[x + i][y + j] == 0:
                return 0
    return 1
def check_posiible(Map,x, y, t):
    if x + t < 10:
        for j in range(t+1):
            if Map[x+t][y+j] == 1:
                return 1
    if y + t < 10:
        for i in range(t+1):
            if Map[x+i][y+t] == 1:
                return 1
    return 0



def fill(Map, x, y, t, val):
    for i in range(t):
        for j in range(t):
            Map[x + i][y + j] = val


def dfs(Map, x, y, cnt):
    global res
    if cnt >= res:
        return
    if sum([sum(x) for x in Map]) == 0:
        res = min(res, cnt)
        return
    for i in range(N):
        for j in range(N):
            # 이부분을 이해하자. 이거떄문에 시간문제걸림
            if 10*i + j < 10*x + y and Map[i][j] == 1:
                return
            if 10 * i + j >= 10 * x + y and Map[i][j] == 1:
                t = 1
                while t < 6:
                    if check_t(Map, i, j, t):
                        t += 1
                    else:
                        break
                # t는 최대 6임 5인경우
                for tt in range(t-1,0,-1):
                    if visit[tt] > 0:
                        visit[tt] -= 1
                        fill(Map, i, j, tt, 0)
                        dfs(Map, i, j, cnt + 1)
                        fill(Map, i, j, tt, 1)
                        visit[tt] += 1


INF = int(1e10)
N = 10
Map = [list(map(int, input().split())) for _ in range(N)]
list_1 = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            list_1.append((i, j))
res = INF
# dfs(Map, x, y, cnt)
visit = [0,5,5,5,5,5]
dfs(Map, 0, 0, 0)
if res == INF:
    print(-1)
else:
    print(res)
