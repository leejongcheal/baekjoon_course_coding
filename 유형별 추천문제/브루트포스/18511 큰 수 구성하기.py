def dfs(now):
    global res
    if len(res) > N_len or int(now) > N:
        return
    if now and int(now) <= N:
        res = str(max(int(res), int(now)))
    for l in L:
        dfs(now+l)


N, cnt = map(int, input().split())
N_len = len(str(N))
L = list(input().split())
same = 1
res = "0"
dfs("0")
print(int(res))
