from collections import defaultdict
def next(x, y):
    y += 1
    if y == 9:
        x += 1
        y = 0
    return x, y
# 가능하면 1 아니면 0
def check(x, y, val):
    if val in Map[x]:
        return 0
    for i in range(9):
        if (x, y) == (i, y):
            continue
        if Map[i][y] == val:
            return 0
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3 + 3):
            if (i,j) == (x, y):
                continue
            if Map[i][j] == val:
                return 0
    return 1
def dfs(x, y): # 조사할 i, j가 주어짐
    global res
    print(x, y)
    if res:
        return
    if x == 9:
        res = Map
        return
    # 채워야 하는경우
    xx, yy = next(x, y)
    if Map[x][y] == 0:
        for a, b in domino:
            if visit[(a, b)] == 0:
                visit[(a, b)] = 1
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 9 and 0 <= ny < 9 and Map[nx][ny] == 0:
                        if check(x,y,a) and check(nx, ny, b):
                            Map[x][y], Map[nx][ny] = a, b
                            dfs(xx, yy)
                        if check(x, y, b) and check(nx, ny, a):
                            Map[x][y], Map[nx][ny] = b, a
                            dfs(xx, yy)
                        Map[x][y], Map[nx][ny] = 0,0
                visit[(a, b)] = 0
    # 안채우고 가도 되는 경우
    else:
        dfs(xx, yy)


INF = int(1e10)
steps = [(0, 1),(1 ,0),(0, -1),(-1, 0)]
while 1:
    domino = []
    for i in range(1, 9):
        for j in range(i+1, 10):
            domino.append((i, j))
    N = int(input())
    if N == 0:
        break
    res = 0
    Map = [[0]*9 for _ in range(9)]
    for _ in range(N):
        a, pos_a, b, pos_b = input().split()
        a, b = int(a), int(b)
        pos_a = [ord(pos_a[0]) - 65, int(pos_a[1]) - 1]
        pos_b = [ord(pos_b[0]) - 65, int(pos_b[1]) - 1]
        Map[pos_a[0]][pos_a[1]] = a
        Map[pos_b[0]][pos_b[1]] = b
        a, b = min(a, b), max(a, b)
        domino.remove((a, b))
    num = list(input().split())
    for i in range(9):
        pos = [ord(num[i][0]) - 65, int(num[i][1]) - 1]
        Map[pos[0]][pos[1]] = i+1
    visit = defaultdict(int)
    dfs(0, 0)
    for m in res:
        print(*m)
