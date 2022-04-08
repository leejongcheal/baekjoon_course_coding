from copy import deepcopy
def slove_sum(Map):
    res = sum([sum(x) for x in Map])*4
    res -= 2*sum(Map[0] + Map[N-1])
    a = b = 0
    for i in range(N):
        a += Map[i][0]
        b += Map[i][M-1]
    res -= 2*(a + b)
    res += Map[0][0] + Map[0][M-1] + Map[N-1][M-1] + Map[N-1][0]
    return res


N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
first_sum = slove_sum(Map)
diff = 0# 이거의 최댓값 찾기
for a in [0, N-1]:
    for b in range(1, N-1):
        new = sum(Map[a])*2 - sum(Map[b])*2 + Map[b][0] + Map[b][M-1] - Map[a][0] - Map[a][M-1]
        diff = max(diff, new)
# 열
for a in [0, M-1]:
    col_a = 0
    for i in range(N):
        col_a += Map[i][a]
    for b in range(1, M-1):
        col_b = 0
        for i in range(N):
            col_b += Map[i][b]
        new = 2*col_a - 2*col_b + Map[0][b] + Map[N-1][b] - Map[0][a] - Map[N-1][a]
        diff = max(diff, new)
print(first_sum + diff)