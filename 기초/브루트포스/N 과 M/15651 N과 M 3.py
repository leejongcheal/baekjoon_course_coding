from itertools import product
n, m = map(int, input().split())
res = list(product(range(1, n+1), repeat=m))
for r in res:
    print(" ".join(map(str, r)))