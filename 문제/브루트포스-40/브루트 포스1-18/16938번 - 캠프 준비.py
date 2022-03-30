from itertools import combinations
from collections import defaultdict
N, L, R, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
res = 0
if N != 1:
    two_index = defaultdict(list)
    for left in range(N - 1):
        for right in range(left + 1, N):
            if A[right] - A[left] >= X:
                two_index[left] = [x for x in range(right, N)]
                break
    for left in two_index.keys():
        for right in two_index[left]:
            now = A[left] + A[right]
            if L <= now <= R:
                res += 1
    if N != 2:
        for i in range(N - 2):
            i += 1
            for left in two_index.keys():
                for right in two_index[left]:
                    now = A[left] + A[right]
                    if right - left - 1 >= i:
                        for comb in combinations(A[left+1: right], i):
                            if L <= now + sum(comb) <= R:
                                res += 1
print(res)