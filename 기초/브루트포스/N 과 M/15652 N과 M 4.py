from itertools import combinations_with_replacement
n, m = map(int, input().split())
res = list(combinations_with_replacement(range(1, n+1), m))
for r in res:
    print(" ".join(map(str, r)))