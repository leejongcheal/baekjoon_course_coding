from itertools import combinations
n, m = map(int, input().split())
L = sorted(list(map(int, input().split())))
res = list(combinations(L, m))
for r in list(res):
    print(" ".join(map(str, r)))