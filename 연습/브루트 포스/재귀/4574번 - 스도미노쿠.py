from collections import defaultdict
from copy import deepcopy
# 가능하면 1 아니면 0
def check(x, y, val):
    if row[x][val]:
        return 0
    if col[y][val]:
        return 0
    if sqare[x//3*3+y//3][val]:
        return 0
    return 1


def dfs(cnt): # 조사할 i, j가 주어짐
    global res
    if res:
        return
    if cnt == E_cnt:
        for m in Map:
            print(*m)
        res = 1
        return
    x, y = E[cnt]
    if Map[x][y]:
        dfs(cnt + 1)
        return
    else:
        for i in range(9):
            for j in range(9):
                if i == j or visit[i][j]:
                    continue
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 9 and 0 <= ny < 9 and Map[nx][ny] == 0:
                        if check(x, y, i) and check(nx, ny, j):
                            Map[x][y], Map[nx][ny] = i + 1, j + 1
                            row[x][i] = row[nx][j] = 1
                            col[y][i] = row[ny][j] = 1
                            sqare[x//3*3 + y//3][i], sqare[nx//3*3 + ny//3][j] = 1, 1
                            visit[i][j] = visit[j][i] = 1
                            dfs(cnt + 1)
                            if res:
                                return
                            Map[x][y], Map[nx][ny] = 0, 0
                            row[x][i] = row[nx][j] = 0
                            col[y][i] = row[ny][j] = 0
                            sqare[x // 3 * 3 + y // 3][i], sqare[nx // 3 * 3 + ny // 3][j] = 0, 0
                            visit[i][j] = visit[j][i] = 0
    return

tc = 1
INF = int(1e10)
steps = [(0, 1),(1 ,0)]
while 1:
    N = int(input())
    if N == 0:
        break
    res = 0
    Map = [[0]*9 for _ in range(9)]
    row = [[0]*9 for _ in range(9)]
    col = [[0]*9 for _ in range(9)]
    sqare = [[0]*9 for _ in range(9)]
    visit = [[0]*9 for _ in range(9)]
    E = []
    for _ in range(N):
        a, pos_a, b, pos_b = input().split()
        a, b = int(a), int(b)
        pos_a = [ord(pos_a[0]) - 65, int(pos_a[1]) - 1]
        pos_b = [ord(pos_b[0]) - 65, int(pos_b[1]) - 1]
        Map[pos_a[0]][pos_a[1]] = a
        row[pos_a[0]][a-1] = 1
        col[pos_a[1]][a-1] = 1
        sqare[pos_a[0]//3 * 3 + pos_a[1]//3][a - 1] = 1
        Map[pos_b[0]][pos_b[1]] = b
        row[pos_b[0]][b - 1] = 1
        col[pos_b[1]][b - 1] = 1
        sqare[pos_b[0] // 3 * 3 + pos_b[1] // 3][b - 1] = 1
        visit[a-1][b-1] = visit[b-1][a-1] = 1
    num = list(input().split())
    for i in range(9):
        pos = [ord(num[i][0]) - 65, int(num[i][1]) - 1]
        Map[pos[0]][pos[1]] = i+1
        row[pos[0]][i] = 1
        col[pos[1]][i] = 1
        sqare[pos[0] // 3 * 3 + pos[1] // 3][i] = 1
    for i in range(9):
        for j in range(9):
            if Map[i][j] == 0:
                E.append((i,j))
    E_cnt = len(E)
    dfs(0)
    print("Puzzle %d"%tc)
    tc += 1
    print(res)
