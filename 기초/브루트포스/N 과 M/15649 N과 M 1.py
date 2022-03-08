from itertools import permutations
n, m = map(int, input().split())
res = list(permutations(range(1, n+1), m))
for r in res:
    print(" ".join(map(str, r)))

