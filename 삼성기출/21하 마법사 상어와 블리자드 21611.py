from collections import defaultdict
def find_L(x, y, t, dx, dy, check):
    for _ in range(t):
        x += dx
        y += dy
        L.append(Map[x][y])
        index[(x, y)] = len(L) - 1
        index[len(L) - 1] = (x, y)
        if check and x == 0 and y == 0:
            return 0, 0
    return x, y
def fill_L(L):
    new_L = [0]
    for l in L[1:]:
        if l != 0:
            new_L.append(l)
    new_L += [0] * (len(L) - len(new_L))
    return new_L
steps = [(-1, 0),(1, 0),(0, -1),(0, 1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
# d, s
blzard = [list(map(int, input().split())) for _ in range(M)]
L = []
index = defaultdict(int)
# L과 index 만들기
x = y = (N-1)//2
t = 0
L.append(Map[x][y])
index[(x, y)] = len(L)-1
index[len(L)-1] = (x, y)
while 1:
    t += 1
    # <-
    x, y = find_L(x, y, t, 0, -1, 1)
    if x == 0 and y == 0:
        break
    # 밑
    x, y = find_L(x, y, t, 1, 0, 0)
    t += 1
    # ->
    x, y = find_L(x, y, t, 0, 1, 0)
    # 위
    x, y = find_L(x, y, t, -1, 0, 0)
res = 0
for idx in range(M):
    # L값에 대해서 Map값 업데이트
    for i in range(len(L)):
        x, y = index[i]
        Map[x][y] = L[i]
    # 블리자드
    d, s = blzard[idx]
    d -= 1
    dx, dy = steps[d]
    x = y = (N-1)//2
    for i in range(s):
        x += dx
        y += dy
        idx = index[(x, y)]
        L[idx] = 0
    # L 빈칸 채우기
    L = fill_L(L)
    # 충돌검사 while 문
    flag = 1 # 충돌있는지 검사용
    while flag:
        flag = 0
        i = 1
        while i < len(L)-1:
            cnt = 1
            if L[i] == L[i+1] and L[i] != 0:
                cnt = 2
                while i+cnt < len(L) and L[i] == L[i+cnt]:
                    cnt += 1
                if cnt >= 4:
                    res += L[i]*cnt
                    flag = 1
                    for j in range(cnt):
                        L[i+j] = 0
            i += cnt
        L = fill_L(L)
    # 1. 충돌 삭제후 빈칸 채우기
    # 2. 충돌있는지 검사
    # 각각의 그룹에 대해서 연산후 L 채우기
    group = [0]
    i = 0
    while i < len(L) - 1:
        cnt = 1
        if L[i] != 0:
            while i + cnt < len(L) and L[i] == L[i + cnt]:
                cnt += 1
            group.append(cnt)
            group.append(L[i])
        i += cnt
    if len(group) > len(L):
        L = group[:len(L)]
    else:
        L = group + [0]*(len(L) - len(group))
print(res)








