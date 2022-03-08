from itertools import product
n, m = map(int, input().split())
L = sorted(list(map(int, input().split())))
res = list(product(L, repeat=m))
for r in list(res):
    print(" ".join(map(str, r)))