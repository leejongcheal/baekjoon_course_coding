from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)
def dfs(L):
    # print(L)
    if L[0] == L[1] == L[2]:
        return 1
    for a, b, c in steps:
        A, B, C = L[a], L[b], L[c]
        B -= A
        A *= 2
        temp = tuple(sorted([A, B , C]))
        if visit[temp] == 0:
            visit[temp] = 1
            if dfs(list(temp)):
                return 1
    return 0


steps = [(0, 1, 2),(0, 2, 1),(1, 2, 0)]
L = list(map(int, input().split()))
L.sort()
visit = defaultdict(int)
visit[tuple(L)] = 1
if dfs(L):
    print(1)
else:
    print(0)
