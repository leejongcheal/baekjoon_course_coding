from collections import deque
def make_str(L):
    s = ""
    for i in range(3):
        for j in range(3):
            s += L[i][j]
    return s
def check(L):
    for i in range(3):
        for j in range(3):
            if L[0][0] != L[i][j]:
                return 0
    return 1
def change_row(i, L):
    temp = [l[::] for l in L]
    for j in range(3):
        temp[i][j] = switch[temp[i][j]]
    visit_check(temp)
def change_col(j, L):
    temp = [l[::] for l in L]
    for i in range(3):
        temp[i][j] = switch[temp[i][j]]
    visit_check(temp)
def change_x(idx, L):
    temp = [l[::] for l in L]
    con = [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    for i, j in con[idx]:
        temp[i][j] = switch[temp[i][j]]
    visit_check(temp)
def visit_check(temp):
    global visit, q, cnt
    s = make_str(temp)
    if s not in visit:
        visit.add(s)
        q.append((temp, cnt + 1))


switch = dict()
switch["H"] = "T"
switch["T"] = "H"
for _ in range(int(input())):
    L = [list(input().split()) for _ in range(3)]
    visit = set()
    s = make_str(L)
    visit.add(s)
    temp = [l[::] for l in L]
    q = deque()
    q.append((temp, 0))
    res = -1
    while q:
        L, cnt = q.popleft()
        if check(L):
            res = cnt
            break
        # row
        for i in range(3):
            change_row(i, L)
            change_col(i, L)
        # x
        change_x(0, L)
        change_x(1, L)
    print(res)