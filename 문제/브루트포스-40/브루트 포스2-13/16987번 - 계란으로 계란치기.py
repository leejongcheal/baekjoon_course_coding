def dfs(now, durability):
    global res
    if now == N:
        break_cnt = 0
        for i in range(N):
            if durability[i] <= 0:
                break_cnt += 1
        res = max(res, break_cnt)
        return
    flag = 0
    if durability[now] <= 0:
        dfs(now+1, durability)
        return
    for i in range(N):
        if i != now and durability[i] > 0:
            flag = 1
            durability[i] -= weight[now]
            durability[now] -= weight[i]
            dfs(now+1, durability)
            durability[i] += weight[now]
            durability[now] += weight[i]
    if flag == 0:
        dfs(now+1, durability)
        return


N = int(input())
# 내구도 무게 순
res = 0
weight = []
durability = []
for _ in range(N):
    d, w = map(int, input().split())
    weight.append(w)
    durability.append(d)
dfs(0, durability)
print(res)
