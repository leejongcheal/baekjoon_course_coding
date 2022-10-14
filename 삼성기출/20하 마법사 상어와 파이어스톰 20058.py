from copy import deepcopy
from collections import deque
def rotate_L(L):
    global N, Map
    temp = [[0]*N for _ in range(N)]
    M = N//L
    for x in range(0, N, L):
        for y in range(0, N, L):
            for i in range(L):
                for j in range(L):
                    temp[x+j][y+L-1-i] = Map[x+i][y+j]
    Map = temp
def check_minus():
    global N, Map, steps
    temp = deepcopy(Map)
    for x in range(N):
        for y in range(N):
            if Map[x][y] == 0:
                continue
            cnt = 0
            for dx, dy in steps:
                nx, ny = x + dx , y + dy
                if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                """
                와 진짜 제발 Map이 도중에 변하면 답이 틀림!!!!!!!!!!!!!!!!!!!!!!!!!
                """
                temp[x][y] -= 1
    Map = temp
def find_set():
    global N, Map, steps, Max_size, visit
    for i in range(N):
        for j in range(N):
            if Map[i][j] > 0 and visit[i][j] == 0:
                size = dfs(i, j)
                Max_size = max(Max_size, size)
def dfs(x, y):
    global N, Map, steps, Max_size, visit
    q = deque()
    visit[x][y] = 1
    cnt = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] >0 and visit[nx][ny] == 0:
                cnt += 1
                visit[nx][ny] = 1
                q.append((nx, ny))
    return cnt

steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
n, Q = map(int, input().split())
N = 2**n
Map = [list(map(int, input().split())) for _ in range(N)]
l_list = list(map(int ,input().split()))
for cnt in range(Q):
    l = l_list[cnt]
    L = 2**l
    rotate_L(L)
    check_minus()
# 합과 최대 덩어리 찾기
Max_size = 0
visit = [[0]*N for _ in range(N)]
find_set()
total = sum([sum(x) for x in Map])
print(total)
print(Max_size)