from collections import deque, defaultdict
from copy import deepcopy
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
def bfs(sx, sy):
    global res, now_key, Map
    q = deque()
    if Map[sx][sy].islower():
        now_key.add(Map[sx][sy])
    visit[(sx, sy)] = len(now_key)
    if Map[sx][sy].isupper() and Map[sx][sy].lower() not in now_key:
        return
    if Map[sx][sy] == "$":
        res.add((sx, sy))
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "*" and visit[(nx,ny)] != len(now_key):
                visit[(nx, ny)] = len(now_key)
                if Map[nx][ny].isupper() and Map[nx][ny].lower() not in now_key:
                    continue
                elif Map[nx][ny].islower():
                    now_key.add(Map[nx][ny])
                elif Map[nx][ny] == "$":
                    res.add((nx, ny))
                q.append((nx, ny))


for tc in range(int(input())):
    N, M = map(int, input().split())
    Map = [list(input()) for _ in range(N)]
    now_key = set(input())
    # if "0" in now_key:
    #     now_key = set()
    start = []
    visit = defaultdict(int)
    res = set()
    for i in range(N):
        if Map[i][0] != "*":
            start.append((i, 0))
        if Map[i][M-1] != "*":
            start.append((i, M-1))
    for j in range(M):
        if Map[0][j] != "*":
            start.append((0, j))
        if Map[N-1][j] != "*":
            start.append((N-1, j))
    # now_key 변화가 없을떄 까지 돌기
    while 1:
        temp = len(now_key)
        for x, y in start:
            if len(now_key) != visit[(x, y)]:
                bfs(x, y)
        if temp == len(now_key):
            break
    print(len(res))
