from copy import deepcopy
def dfs(pre, now):
    global res
    if sum(now) == N:
        val = 0
        for i in range(4):
            val += now[i]*roma[i]
        res.add(val)
        return
    for i in range(pre, 4):
        temp = deepcopy(now)
        temp[i] += 1
        dfs(i, temp)


roma = [1, 5, 10, 50]
N = int(input())
res = set()
dfs(0, [0,0,0,0])
print(len(res))