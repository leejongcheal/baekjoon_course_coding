import copy
def rotate_90(rota):
    N, M = len(rota), len(rota[0])
    rrota = [[0]*N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            rrota[j][N-1-i] = rota[i][j]
    return rrota
def rotate_180(rota):
    N, M = len(rota), len(rota[0])
    rrota = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            rrota[N-1-i][M-1-j] = rota[i][j]
    return rrota
def bal(LL, steps):
    temp = copy.deepcopy(LL)
    for i in range(len(LL)):
        for j in range(len(LL[i])):
            for dx, dy in steps:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(LL) and 0 <= nj < len(LL[ni]):
                    d = abs(LL[i][j] - LL[ni][nj]) // 5
                    if LL[i][j] < LL[ni][nj]:
                        d = -1 * d
                    temp[i][j] -= d
                    temp[ni][nj] += d
    return temp
steps = [(0, 1),(1,0)]
N, K = map(int, input().split())
L = list(map(int, input().split()))
cnt = 0
M, m = max(L), min(L)
while M- m > K:
    cnt += 1
    # 작은 물고기 + 1
    m = min(L)
    for i in range(len(L)):
        if L[i] == m:
            L[i] += 1
    # 한칸 올리기
    LL = []
    LL.append([L[0]])
    LL.append(L[1:])
    # 높이 2개이상 90도 회전
    H = len(LL)
    W = len(LL[0])
    R = len(LL[-1]) - W
    while R >= H:
        rota = []
        for i in range(H):
            rota.append(LL[i][:W])
        re_l = LL[-1][W:]
        rota = rotate_90(rota)
        rota.append(re_l)
        LL = rota
        H = len(LL)
        W = len(LL[0])
        R = len(LL[-1]) - W
    # 인접물고기 계산
    LL = bal(LL,steps)
    temp = []
    # 일자 배열
    for j in range(len(LL[-1])):
        temp.append(LL[-1][j])
        if 0 <= j < len(LL[0]):
            for i in range(len(LL)-2, -1,-1):
                temp.append(LL[i][j])
    LL = temp
    # 공중배열 2번
    L = LL[:len(LL)//2]
    R = LL[len(LL)//2:]
    rota = rotate_180([L])
    rota.append(R)
    LL = rota
    L = []
    R = []
    for l in LL:
        L.append(l[:len(l)//2])
        R.append(l[len(l)//2:])
    rota = rotate_180(L)
    for r in R:
        rota.append(r)
    LL = rota
    # 두번 회전후 밸런스
    LL = bal(LL,steps)
    temp = []
    for j in range(len(LL[0])):
        for i in range(len(LL)-1,-1,-1):
            temp.append(LL[i][j])
    L = temp
    M, m = max(L), min(L)
print(cnt)