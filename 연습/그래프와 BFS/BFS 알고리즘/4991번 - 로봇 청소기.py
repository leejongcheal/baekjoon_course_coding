from collections import deque
import heapq
INF = int(1e10)
steps = [(1, 0),(0, 1),(-1, 0),(0, -1)]
res = INF


def dfs(L, now, dist, visit):
    global res
    # if visit.count(1) == len(visit):
    if dist > res:
        return
    if sum(visit) == len(visit):
        res = min(res, dist)
        return
    for i in range(len(visit)):
        if visit[i] == 0:
            visit[i] = 1
            dfs(L, i,dist + L[now][i], visit)
            visit[i] = 0


def solve(Map, N, M):
    global res
    res = INF
    min_val = INF
    position_index = dict()
    index = 1
    L = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == "o":
                position_index[0] = (i,j)
            if Map[i][j] == "*":
                position_index[index] = (i, j)
                index += 1
    # print(position_index)
    length = len(position_index.keys())
    for i in range(length):
        sx, sy = position_index[i]
        dist = [[INF]*M for _ in range(N)]
        dist[sx][sy] = 0
        q = [(0, sx, sy)]
        while q:
            now_dist, x, y = heapq.heappop(q)
            if now_dist > dist[x][y]:
                continue
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "x":
                    if now_dist + 1 < dist[nx][ny]:
                        dist[nx][ny] = now_dist + 1
                        heapq.heappush(q,(dist[nx][ny], nx, ny))
        temp = []
        for i in range(length):
            x, y = position_index[i]
            if dist[x][y] == INF:
                return -1
            temp.append(dist[x][y])
        L.append(temp)
    visit = [0]*length
    visit[0] = 1
    dfs(L, 0, 0, visit)
    return res


while 1:
    M, N = map(int,input().split())
    if N == 0 and M == 0:
        break
    Map = [list(input()) for _ in range(N)]
    print(solve(Map, N, M))