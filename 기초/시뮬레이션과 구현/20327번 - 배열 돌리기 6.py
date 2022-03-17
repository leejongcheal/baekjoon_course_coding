def split(Map, l):
    global N
    M = 2**l
    cnt = N//M
    temp = [[[[0]*M for z in range(M)] for x in range(cnt)] for c in range(cnt)]
    for i in range(cnt):
        for j in range(cnt):
            sub = temp[i][j]
            for x in range(M):
                for y in range(M):
                    sub[x][y] = Map[i*M + x][j*M + y]
    return temp

def fill(Map, sub_list):
    global N
    M = 2**l
    cnt = N // M
    for i in range(cnt):
        for j in range(cnt):
            sub = sub_list[i][j]
            for x in range(M):
                for y in range(M):
                    Map[x + i*M][y + j*M] = sub[x][y]
def rotate(L):
    length = len(L)
    temp = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[j][length - 1 - i] = L[i][j]
    return temp
def reverse_rotate(L):
    length = len(L)
    temp = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[length - 1 - j][i] = L[i][j]
    return temp
def up_down(L):
    length = len(L)
    for j in range(length):
        for i in range(length//2):
            L[i][j], L[length - 1 - i][j] = L[length - 1 - i][j], L[i][j]
    return L
def reverse(L):
    length = len(L)
    for i in range(length):
        for j in range(length//2):
            L[i][j], L[i][length - 1 - j] = L[i][length - 1 - j], L[i][j]
    return L


n, R = map(int, input().split())
N = 2**n
Map = [list(map(int, input().split())) for _ in range(N)]
R_list = []
for _ in range(R):
    R_list.append(tuple(map(int,input().split())))
for k, l in R_list:
    # 나누기
    sub_list = split(Map,l)
    if k < 5:
        cnt = N // 2**l
        if k == 1:
            for i in range(cnt):
                for j in range(cnt):
                    sub_list[i][j] = up_down(sub_list[i][j])

        elif k == 2:
            for i in range(cnt):
                for j in range(cnt):
                    sub_list[i][j] = reverse(sub_list[i][j])
        elif k == 3:
            for i in range(cnt):
                for j in range(cnt):
                    sub_list[i][j] = rotate(sub_list[i][j])
        elif k == 4:
            for i in range(cnt):
                for j in range(cnt):
                    sub_list[i][j] = reverse_rotate(sub_list[i][j])
    elif k >= 5:
        if k == 5:
            sub_list = up_down(sub_list)
        elif k == 6:
            sub_list = reverse(sub_list)
        elif k == 7:
            sub_list = rotate(sub_list)
        elif k == 8:
            sub_list = reverse_rotate(sub_list)
    fill(Map, sub_list)
    # 확인
for m in Map:
    print(" ".join(map(str, m)))