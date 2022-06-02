from collections import defaultdict
def dfs(i, split):
    global res
    if i == N - 1:
        value = 1
        for v in split:
            value *= v
        res = max(res, value)
        return
    i += 1
    for idx in range(len(split)):
        temp = split[::]
        temp[idx] += L[i]
        dfs(i, temp)


N = int(input())
L = list(map(int, input().split()))
P, Q = map(int, input().split())
visit = defaultdict(set)
split = [0]*(Q+1)
res = 0
dfs(-1, split)
print(res)
