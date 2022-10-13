from collections import defaultdict
def remove(cnt):
    global steps,shark_move, shark_steps, N, remove_index, L_index, L_value
    x, y = N//2, N//2
    d, s = shark_move[cnt]
    dx, dy = shark_steps[d]
    for i in range(1, s+1):
        x += dx
        y += dy
        idx = L_index[(x, y)]
        L_value[idx] = 0
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
                L_value.append(Map[x][y])
                L_index[(x, y)] = len(L_value) - 1
                L_index[(len(L_value))-1] = (x, y)
def fill():
    global Map, steps, N, L_value, L_index, remove_index
    L_new = []
    for i in range(len(L_value)):
        if L_value[i] != 0:
            L_new.append(L_value[i])
    L_new += [0]*(N*N-1 -len(L_new))
    L_value = L_new
def bomb():
    global Map, steps, N, L_value, L_index, remove_index, res
    flag = 0
    i = 0
    while i < len(L_value)-1:
        cnt = 1
        if L_value[i] == L_value[i+cnt] and L_value[i]!= 0:
            cnt = 2
            while i + cnt < len(L_value) and L_value[i] == L_value[i+cnt]:
                cnt += 1
            if cnt >= 4:
                res[L_value[i]] += cnt
                flag = 1
                for j in range(cnt):
                    L_value[i+j] = 0
        i += cnt
    fill()
    return flag
def change():
    global Map, steps, N, L_value, L_index, remove_index, res
    '''
    아예 값이 없어서 안채워야 하는 경우 고려를 못함
    L_value = [0,0,0,0...]인경우에도 
    L[0] 을 초기화 시키고 시작하면 
    cnt = 1 고정이 되어버 0,1 이들어가는 경우가 생김을 주의
    '''
    i = 0
    new = []
    while i < len(L_value) - 1 and L_value[i] != 0:
        cnt = 1
        if L_value[i] == L_value[i+cnt]:
            cnt = 2
            while i+cnt < len(L_value) and L_value[i] == L_value[i+cnt]:
                cnt += 1
        new.append(cnt)
        new.append(L_value[i])
        i += cnt
    if len(new) > len(L_value):
        L_value = new[:len(L_value)]
    else:
        L_value = new + [0]*(len(L_value) - len(new))


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
L_index = defaultdict()
make_index()
remove_index = set()
for cnt in range(M):
    # 구슬삭제
    remove(cnt)
    # 채우기
    fill()
    # 구슬 폭팔
    while 1:
        flag = bomb()
        if flag == 0:
            break
    # 구슬 변환
    change()

total = sum([i*res[i] for i in range(4)])
print(total)