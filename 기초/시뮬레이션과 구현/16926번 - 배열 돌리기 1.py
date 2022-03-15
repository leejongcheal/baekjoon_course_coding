def fill(Map, temp, N, M, x, y):
    level = x
    #밑으로
    i, j = level, level
    for i in range(level, N-1-level):
        temp[i+1][j] = Map[i][j]
    #오른쪽으로
    i,j = N-1-level, level
    for j in range(level, M-1-level):
        temp[i][j+1] = Map[i][j]
    #위로
    i, j = N-1-level, M-1-level
    for i in range(N-1-level,level, -1):
        temp[i-1][j] = Map[i][j]
    #왼쪽으로
    i, j = level, M - 1 - level
    for j in range(M-1-level,level, -1):
        temp[i][j-1] = Map[i][j]
    # print(str(i)+"시작한 결과")
    # for t in temp:
    #     print(t)


def rotate(Map, N, M):
    temp = [[0]*M for _ in range(N)]
    for i in range(min(N, M) // 2):
        fill(Map, temp, N, M, i, i)
    return temp


N, M, R = map(int,input().split())
Map = [list(input().split()) for _ in range(N)]
for _ in range(R):
    Map = rotate(Map, N, M)
for m in Map:
    print(" ".join(m))