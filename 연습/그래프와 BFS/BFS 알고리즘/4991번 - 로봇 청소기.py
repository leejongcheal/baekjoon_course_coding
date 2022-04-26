from collections import deque
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
INF = int(1e10)


def bfs(dist, Map, x, y, tr_pos):
    visit = [[INF]*M for _ in range(N)]
    q = deque()
    q.append((x,y))
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] > visit[x][y] + 1 and Map[nx][ny] != "x":
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    for idx, (x, y) in enumerate(tr_pos):
        dist[idx] = visit[x][y]


def find_dists():
    tr_pos = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == "*":
                tr_pos.append((i,j))
            elif Map[i][j] == "o":
                tr_pos = [(i, j)] + tr_pos
    dists = []
    tr_cnt = len(tr_pos)
    for idx, (x, y) in enumerate(tr_pos):
        dist = [INF]*tr_cnt
        bfs(dist, Map, x, y, tr_pos)
        if INF in dist:
            return -1
        dists.append(dist)
    return dists


def dfs(now, cnt, visit, val): # now_idx, cnt, visit, val
    global res
    if cnt == dist_len:
        res = min(res, val)
        return
    if val + min_dist*(dist_len-cnt) > res:
        return
    for next in range(dist_len):
        if visit[next] == 0:
            visit[next] = 1
            dfs(next, cnt + 1, visit, val + dists[now][next])
            visit[next] = 0



while 1:
    M, N = map(int, input().split())
    if N == M == 0:
        break
    Map = [list(input()) for _ in range(N)]
    dists = find_dists()
    if dists == -1:
        print(dists)
    else:
        res = INF
        # dists 구했으니 이걸토대로 가장 짧은 길이 구하기 dfs사용하자.
        dist_len = len(dists)
        visit = [0]*dist_len
        min_dist = INF
        for dist in dists:
            for d in dist:
                if d != 0:
                    min_dist = min(d, min_dist)
        visit[0] = 1
        res = INF
        dfs(0, 1, visit, 0) # now_idx, cnt, visit, val
        print(res)