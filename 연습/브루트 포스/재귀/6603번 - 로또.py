from itertools import combinations
while 1:
    L = list(map(int, input().split()))
    if len(L) == 1 and L[0] == 0:
        break
    for comb in list(combinations(L[1:], 6)):
        print(*comb)
    print()