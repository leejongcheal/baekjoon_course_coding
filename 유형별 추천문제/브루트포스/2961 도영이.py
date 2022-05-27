from itertools import combinations
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
res = INF = int(1e10)
for cnt in range(1, N+1):
    for choice in combinations(range(N), cnt):
        sum_s, sum_b= 1, 0
        for c in choice:
            sum_s *= L[c][0]
            sum_b += L[c][1]
        res = min(res, abs(sum_s - sum_b))
print(res)
