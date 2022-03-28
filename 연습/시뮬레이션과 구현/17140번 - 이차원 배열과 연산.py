from collections import Counter


def r_oper(Map):
    L = []
    N, M = len(Map), len(Map[0])
    for i in range(N):
        c = Counter()
        now = Counter(Map[i])
        c[0] = now[0]
        now = now - c
        now = list(now.items())
        now.sort(key=lambda x: (x[1], x[0]))
        M = max(len(now) * 2, M)
        L.append(now)
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(len(L[i])):
            if j < 50:
                temp[i][2 * j], temp[i][2 * j + 1] = L[i][j][0], L[i][j][1]
    return temp

def c_oper(Map):
    L = []
    N, M = len(Map), len(Map[0])
    temp_N = N
    for j in range(M):
        t = []
        for i in range(N):
            if Map[i][j] != 0:
                t.append(Map[i][j])
        now = list(Counter(t).items())
        now.sort(key = lambda x: (x[1], x[0]))
        temp_N = max(len(now) * 2, temp_N)
        L.append(now)
    temp = [[0] * M for _ in range(temp_N)]
    for j in range(M):
        for i in range(len(L[j])):
            temp[2*i][j], temp[2*i + 1][j] = L[j][i][0], L[j][i][1]
    return temp


r, c, k = map(int, input().split())
r -= 1
c -= 1
Map = [list(map(int, input().split())) for _ in range(3)]
time = 0
res = -1
while time <= 100:
    N, M = len(Map), len(Map[0])
    if 0 <= r < N and 0 <= c < M and Map[r][c] == k:
        res = time
        break
    if N >= M:
        Map = r_oper(Map)
    elif M > N:
        Map = c_oper(Map)
    time += 1
    N, M = len(Map), len(Map[0])
    if N > 100:
        temp = []
        for i in range(100):
            temp.append(Map[i])
        Map = temp
    if M > 100:
        for i in range(N):
            Map[i] = Map[i][:100]
print(res)
