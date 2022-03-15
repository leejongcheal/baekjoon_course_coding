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
def split(Map, level, n, m):
    line = []
    i,j = level, level
    for j in range(level, level + m -1):
        line.append(Map[i][j])
    i,j=level,level+m-1
    for i in range(level,level + n - 1):
        line.append(Map[i][j])
    i,j=level + n -1, level+m-1
    for j in range(level+m-1,level,-1):
        line.append(Map[i][j])
    i,j = level+n-1, level
    for i in range(level+n-1,level,-1):
        line.append(Map[i][j])
    return line


def fill(res,temp, level, n, m):
    i, j = level, level
    index = 0
    for j in range(level, level + m - 1):
        res[i][j] = temp[index]
        index += 1
    i, j = level, level + m - 1
    for i in range(level, level + n - 1):
        res[i][j] = temp[index]
        index += 1
    i, j = level + n - 1, level + m - 1
    for j in range(level + m - 1, level, -1):
        res[i][j] = temp[index]
        index += 1
    i, j = level + n - 1, level
    for i in range(level + n - 1, level, -1):
        res[i][j] = temp[index]
        index += 1


def rotate(Map, N, M,R):
    res = [[0]*M for _ in range(N)]
    lines = []
    for i in range(min(N, M) // 2):
        lines.append(split(Map, i, N - 2*i, M - 2*i))
    temps = []
    for line in lines:
        move_index = R % len(line)
        temp = line[move_index:] + line[:move_index]
        temps.append(temp)
    for i in range(min(N, M) // 2):
        fill(res,temps[i], i, N - 2 * i, M - 2 * i)
    return res


N, M, R = map(int,input().split())
Map = [list(input().split()) for _ in range(N)]
Map = rotate(Map, N, M, R)
for m in Map:
    print(" ".join(m))