def rotate(sticker):
    n, m = len(sticker), len(sticker[0])
    temp = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j][n-1-i] = sticker[i][j]
    return temp
def check(x, y, sticker):
    n,m = len(sticker), len(sticker[0])
    flag = 0
    for i in range(n):
        for j in range(m):
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M:
                if sticker[i][j] == 1:
                    if Map[nx][ny] == 1:
                        return 0
            else:
                return 0
    for i in range(n):
        for j in range(m):
            nx, ny = x + i, y + j
            if sticker[i][j] == 1:
                Map[nx][ny] = 1
    return 1
N, M, sticker_cnt = map(int, input().split())
sticker_list = []
for _ in range(sticker_cnt):
    sn, sm = map(int, input().split())
    sticker_list.append([list(map(int, input().split())) for _ in range(sn)])
Map = [[0]*M for _ in range(N)]
for sticker in sticker_list:
    flag = 0
    for i in range(4):
        if i != 0:
            sticker = rotate(sticker)
        for i in range(N):
            for j in range(M):
                flag = check(i,j, sticker)
                if flag:
                    break
            if flag:
                break
        if flag:
            break
res = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            res += 1
print(res)