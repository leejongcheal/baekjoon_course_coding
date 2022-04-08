from collections import deque
def find(L):
    global parent
    x, y = L
    if parent[x][y] == L:
        return [x, y]
    parent[x][y] = find(parent[x][y])
    return parent[x][y]

def union(a, b): # 리스트형태로 넣어주기
    global parent
    A = find(a)
    B = find(b)
    ax, ay = A
    bx, by = B
    if Map[ax][ay] > Map[bx][by]:
        parent[ax][ay] = B
    else:
        parent[bx][by] = A

INF = 1e10
steps = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
parent = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        parent[i][j] = [i, j]
for i in range(N):
    for j in range(M):
        if find([i,j]) == [i, j]:
            x, y = i, j
            while 1: # 이동이 없을떄까지 검사
                min_val = Map[x][y]
                mx, my = -1, -1
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] < min_val:
                        min_val = Map[nx][ny]
                        mx, my = nx, ny
                if mx != -1:
                    union([i, j], [mx, my])
                    break
                elif mx == -1:
                    break
res = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        x, y = find([i, j])
        res[x][y] += 1
for r in res:
    print(*r)