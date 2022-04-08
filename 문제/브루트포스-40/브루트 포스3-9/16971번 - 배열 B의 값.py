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

res = 0
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
first_sum = max(slove_sum(Map), res)
diff = 0 # 이거의 최댓값 찾기
#  행 조사
n = 0
for i in range(N):
    diff = max(diff, 2*sum(Map[n]) - Map[n][0] - Map[n][M-1] - 2*sum(Map[i]) + Map[i][0] + Map[i][M-1])

n = N - 1
for i in range(N):
    diff = max(diff, 2*sum(Map[n]) - Map[n][0] - Map[n][M-1] - 2*sum(Map[i]) + Map[i][0] + Map[i][M-1])

# 열 조사
m = 0
sum_m = 0
for i in range(N):
    sum_m += Map[i][m]
for i in range(M):
    sum_i = 0
    for j in range(N):
        sum_i += Map[j][i]
    diff = max(diff, 2*sum_m - 2*sum_i - Map[0][m] - Map[N-1][m] + Map[0][i] + Map[N-1][i])

m = M-1
sum_m = 0
for i in range(N):
    sum_m += Map[i][m]
for i in range(M):
    sum_i = 0
    for j in range(N):
        sum_i += Map[j][i]
    diff = max(diff, 2*sum_m - 2*sum_i - Map[0][m] - Map[N-1][m] + Map[0][i] + Map[N-1][i])
print(first_sum + diff)