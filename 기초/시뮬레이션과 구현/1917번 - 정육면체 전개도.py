cubes = [
    [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]],
    [[0, 1, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]],
    [[0, 0, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0]],
    [[0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0]],
    [[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]],
    [[0, 0, 1, 0], [1, 1, 1, 1], [0, 1, 0, 0]],
    [[0, 0, 1, 1, 1], [1, 1, 1, 0, 0]],
    [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0]],
    [[0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 0, 0]],
    [[1, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]],
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1]]
]


def rotate(L):
    N, M = len(L), len(L[0])
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            temp[j][N - 1 - i] = L[i][j]
    return temp
def reverse(L):
    N, M = len(L), len(L[0])
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[N-1-i][j] = L[i][j]
    return temp


def check(cube, Map):
    N, M = len(cube), len(cube[0])
    for i in range(6):
        for j in range(6):
            cnt = 0
            for x in range(N):
                for y in range(M):
                    if 0 <= x + i < 6 and 0 <= y + j < 6:
                        if cube[x][y] == Map[x + i][y + j]:
                            cnt += 1
            if cnt == N*M:
                return 1
    return 0


for _ in range(3):
    Map = [list(map(int, input().split())) for _ in range(6)]
    flag = 0
    for cube in cubes:
        for _ in range(2):
            cube = reverse(cube)
            for i in range(4):
                cube = rotate(cube)
                if flag:
                    continue
                if check(cube, Map) == 1:
                    flag = 1
    if flag:
        print("yes")
    else:
        print("no")
