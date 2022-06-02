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
    flag = 0
    for idx in range(len(split)):
        temp = split[::]
        if temp[idx] == 0:
            flag = 1
        temp[idx] += L[i]
        dfs(i, temp)
        if flag:
            break

N = int(input())
L = list(map(int, input().split()))
P, Q = map(int, input().split())
visit = defaultdict(set)
split = [0]*(Q+1)
res = 0
dfs(-1, split)
print(res)
