# 아 시이발 좆같네 진짜 어쩌라고  그래서
# 끝나는 기준도 애매하고 다채웠는지 확인하고싶은데도 못하고 돌다가 못채우는 경우는 없다고 가정을 치자
# 그래서 끝날떄 까지 visit인 set에 계속 채워놓고 cnt를 계산하고 다음부터 min_index를 채우면됨
# 그러면 전의 최소값은 어쩔껀데 ㅋㅋ min_index를  갯수를 세고

def check(x, y, val):
    global steps, N, Map
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0<= ny < N and Map[nx][ny] == val:
            return 0
    return 1

def dfs(x, y, index, val, cnt):
    # print(index, cnt)
    # cnt는 그린거의 갯수, val 은 들어갈 값
    global steps, min_index, M, Map, N, visit
    if index >= min_index:
        return
    if cnt == M:
        # print(1)
        min_index = min(min_index, index)
        return
    Map[x][y] = val
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == "X":
            flag = 1
            for i in range(index):
                if check(nx, ny, i):
                    flag = 0
                    dfs(nx, ny, index, i, cnt + 1)
            if flag:
                dfs(nx, ny, index + 1, index, cnt + 1)
    Map[x][y] = "X"

def dfs_first(x, y):
    visit.add((x, y))
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == "X":
            if (nx, ny) not in visit:
                dfs_first(nx, ny)


steps = [(-1, 0),(-1, 1),(0, 1),(1, 0),(1, -1),(0, -1)]
N = int(input())
location = []
Map = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Map[i][j] == "X":
            location.append((i, j))
res = 10**10
M = len(location)
cnt = 0
visit = set()
visited = [[0]*N for _ in range(N)]
for x, y in location:
    if Map[x][y] == "X" and visited[x][y] == 0:
        visit = set()
        dfs_first(x, y)
        M = len(visit)
        for vx, vy in visit:
            visited[vx][vy] = 1
        # print(visit)
        # print(M)
        min_index = 10**10
        cnt = 1
        dfs(x, y, 1, 0, cnt)
        res = min(min_index, res)
if location:
    print(res)
else:
    print(0)