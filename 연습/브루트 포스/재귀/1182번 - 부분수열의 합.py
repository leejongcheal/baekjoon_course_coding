from itertools import combinations
ans = 0
N, S = map(int, input().split())
L = list(map(int, input().split()))
for i in range(1, N + 1):
    for comb in combinations(L, i):
        if sum(comb) == S:
            ans += 1
print(ans)