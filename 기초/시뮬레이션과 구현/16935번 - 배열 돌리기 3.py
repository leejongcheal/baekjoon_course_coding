def oper_1(Map, N, M): # 상하 반전
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[N-1-i][j] = Map[i][j]
    return temp

def oper_2(Map, N, M): # 좌우반전
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][M-1-j] = Map[i][j]
    return temp
def oper_3(Map, N, M): # 오른쪽 90도 회전
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            temp[j][N-1-i] = Map[i][j]
    return temp
def oper_4(Map, N, M): # 왼쪽 90도 회전
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            temp[M-1-j][i] = Map[i][j]
    return temp
def split_4(Map, N, M):
    Map1 = [[0]*(M//2) for _ in range(N//2)]
    Map2 = [[0]*(M//2) for _ in range(N//2)]
    Map3 = [[0]*(M//2) for _ in range(N//2)]
    Map4 = [[0]*(M//2) for _ in range(N//2)]
    for i in range(N):
        for j in range(M):
            if 0 <= i < N // 2 and 0 <= j < M // 2:
                Map1[i][j] = Map[i][j]
            elif 0 <= i < N // 2 and M // 2 <= j < M:
                Map2[i][j - M//2] = Map[i][j]
            elif N // 2 <= i < N and 0 <= j < M // 2:
                Map4[i - N//2][j] = Map[i][j]
            elif N // 2 <= i < N and M // 2 <= j < M:
                Map3[i - N//2][j - M//2] = Map[i][j]
    return Map1, Map2, Map3, Map4

def oper_5(Map, N, M):
    Map1, Map2, Map3, Map4 = split_4(Map, N, M)
    temp = []
    for i in range(N):
        if i < N // 2:
            temp.append(Map4[i] + Map1[i])
        else:
            temp.append(Map3[i- N // 2] + Map2[i - N // 2])
    return temp
def oper_6(Map, N, M):
    Map1, Map2, Map3, Map4 = split_4(Map, N, M)
    temp = []
    for i in range(N):
        if i < N // 2:
            temp.append(Map2[i] + Map3[i])
        else:
            temp.append(Map1[i - N // 2] + Map4[i - N // 2])
    return temp


N, M, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
oper_list = list(map(int, input().split()))
for oper in oper_list:
    N, M = len(Map), len(Map[0])
    if oper == 1:
        Map = oper_1(Map, N, M)
    elif oper == 2:
        Map = oper_2(Map, N, M)
    elif oper == 3:
        Map = oper_3(Map, N, M)
    elif oper == 4:
        Map = oper_4(Map, N, M)
    elif oper == 5:
        Map = oper_5(Map, N, M)
    elif oper == 6:
        Map = oper_6(Map, N, M)
for x in Map:
    print(" ".join(map(str, x)))
