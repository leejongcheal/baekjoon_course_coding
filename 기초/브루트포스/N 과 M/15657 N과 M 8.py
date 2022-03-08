from itertools import combinations_with_replacement
n, m = map(int, input().split())
L = sorted(list(map(int, input().split())))
res = list(combinations_with_replacement(L, m))
for r in list(res):
    print(" ".join(map(str, r)))