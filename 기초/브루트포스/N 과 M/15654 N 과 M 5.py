from itertools import permutations
n, m = map(int, input().split())
L = list(map(int, input().split()))
res = list(permutations(L, m))
for r in sorted(list(res)):
    print(" ".join(map(str, r)))