def dfs(L):
    global max_val, min_val, sign, n
    cnt = len(L) - 1
    if cnt == n:
        s = "".join(map(str, L))
        max_val = max(max_val, s)
        min_val = min(min_val, s)
        return
    for i in range(10):
        if visit[i] == 0:
            if (sign[cnt] == "<" and L[-1] < i) or (sign[cnt] == ">" and L[-1] > i):
                visit[i] = 1
                dfs(L + [i])
                visit[i] = 0


n = int(input())
sign = list(input().split())
max_val = "0"
min_val = "9999999999999999999999"
visit = [0]*10
for i in range(10):
    visit[i] = 1
    dfs([i])
    visit[i] = 0
print(max_val)
print(min_val)