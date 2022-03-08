from itertools import combinations
n, m = map(int, input().split())
res = list(combinations(range(1, n+1), m))
for r in res:
    print(" ".join(map(str, r)))