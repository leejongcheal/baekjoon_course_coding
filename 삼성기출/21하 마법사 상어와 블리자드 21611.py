def make_remove_index(cnt):
    global steps,shark_move, shark_steps, N, remove_index
    x, y = N//2, N//2
    d, s = shark_move[cnt]
    dx, dy = shark_steps[d]
    remove_index = set()
    for i in range(1, s+1):
        x += dx
        y += dy
        remove_index.add((x, y))
def make_index():
    global Map, steps, N, L_value, L_index, steps
    x, y = N//2, N//2
    now = 0
    while 1:
        now +=1
        for i in range(4):
            if i == 2:
                now += 1
            dx, dy = steps[i]
            for _ in range(now):
                x += dx
                y += dy
                if i == 0:
                    if not (0 <= x < N and 0 <= y < N):
                        return
                L_index.append((x, y))
def make_value():
    global Map, steps, N, L_value, L_index, steps
    L_value = [0]*(N*N - 1)
    for i, (x, y) in enumerate(L_index):
        if Map[x][y] == 0:
            return
        L_value[i] = Map[x][y]
def remove():
    global Map, steps, N, L_value, L_index, remove_index
    L_new = []
    for i, (x, y) in enumerate(L_index):
        if (x, y) in remove_index:
            continue
        L_new.append(L_value[i])
    L_new += [0]*(N*N-1-len(L_new))
    L_value = L_new
def bomb():
    global Map, steps, N, L_value, L_index, remove_index, res
    flag = 0
    i = 1
    L_new = []
    if L_value[0] == 0:
        L_value = [0]*(N*N-1)
        return
    pre = L_value[0]
    cnt = 1
    while i < len(L_value) and L_value[i] != 0:
        if pre != L_value[i] and cnt < 4:
            L_new += [pre]*cnt
            pre = L_value[i]
            cnt = 1
        elif pre != L_value[i] and cnt >= 4:
            res[pre] += cnt
            flag = 1
            pre = L_value[i]
            cnt = 1
        elif pre == L_value[i]:
            cnt += 1
        i += 1
    if cnt < 4:
        L_new += [pre] * cnt
    else:
        res[pre] += cnt
        flag = 1
    L_new += [0] * (N * N - 1 - len(L_new))
    L_value = L_new
    return flag
def change():
    global Map, steps, N, L_value, L_index, remove_index, res
    L_new = []
    '''
    아예 값이 없어서 안채워야 하는 경우 고려를 못함
    L_value = [0,0,0,0...]인경우에도 
    cnt = 1 고정이 되버림...시발
    '''
    if L_value[0] == 0:
        L_value = [0]*(N*N-1)
        return
    pre = L_value[0]
    cnt = 1
    i = 1
    while i < len(L_value) and L_value[i] != 0 and len(L_new) < N*N:
        if pre != L_value[i]:
            L_new.append(cnt)
            L_new.append(pre)
            pre = L_value[i]
            cnt = 1
        elif pre == L_value[i]:
            cnt += 1
        i += 1
    L_new.append(cnt)
    L_new.append(pre)
    if len(L_new) >= N*N:
        L_new = L_new[:N*N-1]
    else:
        L_new += [0] * (N * N - 1 - len(L_new))
    L_value = L_new
steps = [(0, -1),(1, 0),(0, 1),(-1,0)]
shark_steps = [(-1, 0),(1, 0),(0, -1),(0, 1)]
N, M = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))
shark_move = []
for _ in range(M):
    d, s = map(int, input().split())
    shark_move.append((d-1, s))
res = [0,0,0,0]
L_value = []
L_index = []
make_index()
make_value()
remove_index = set()
for cnt in range(M):
    # 삭제할 인덱스 만들기
    make_remove_index(cnt)
    # 구슬삭제
    remove()
    # 구슬 폭팔
    while 1:
        flag = bomb()
        if flag == 0:
            break
    # 구슬 변환
    change()

total = sum([i*res[i] for i in range(4)])
print(total)