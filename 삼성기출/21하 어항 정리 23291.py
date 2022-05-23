def balence(L):
    value = [[0] * len(L[-1]) for _ in range(len(L))]
    for x in range(len(L)):
        for y in range(len(L[x])):
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(L) and 0 <= ny < len(L[nx]):
                    d = abs(L[x][y] - L[nx][ny]) // 5
                    if L[x][y] > L[nx][ny]:
                        value[x][y] -= d
                        value[nx][ny] += d
                    else:
                        value[x][y] += d
                        value[nx][ny] -= d
    for x in range(len(L)):
        for y in range(len(L[x])):
            L[x][y] += value[x][y]
    for x in range(len(L)):
        L[x] += ["#"] * (len(L[-1]) - len(L[x]))
    New = []
    for y in range(len(L[x])):
        for x in range(len(L) - 1, -1, -1):
            if L[x][y] != "#":
                New.append(L[x][y])
    L = New
    return L
steps = [(0, 1),(1, 0)]
N, K = map(int, input().split())
L = list(map(int, input().split()))
M, m = max(L), min(L)
cnt = 0
while M - m > K:
    cnt += 1
    New = []
    # 최솟값 += 1
    m = min(L)
    for i in range(len(L)):
        if L[i] == m:
            L[i] += 1
    # 하나 위로 올리기
    New = []
    New.append([L[0]])
    New.append(L[1:])
    L = New
    # 90회전
    while 1:
        h, w = len(L), len(L[0])
        if len(L[-1]) - w < h:
            break
        New = [[0]*h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                New[j][h-1-i] = L[i][j]
        temp = L[-1][w:]
        New.append(temp)
        L = New
    # 물고기수 조절
    L = balence(L)
    split = L[:len(L)//2]
    New = []
    New.append(split[::-1])
    New.append(L[len(L)//2:])
    L = New
    n, m = len(L), len(L[0]) // 2
    split = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            split[-(i+1)][-(j+1)] = L[i][j]
    for i in range(n):
        split.append(L[i][m:])
    L = split
    L = balence(L)
    M, m = max(L), min(L)
print(cnt)

