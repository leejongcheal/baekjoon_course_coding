from itertools import combinations
while 1:
    L = list(map(int ,input().split()))
    n, L = L[0], L[1:]
    if n == 0:
        break
    for comb in combinations(L, 6):
        print(" ".join(map(str, comb)))
    print()