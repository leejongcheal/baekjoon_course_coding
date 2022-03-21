def dfs(now, cnt):
    global Max, Min, L, oper, N
    if cnt == N:
        Max = max(Max, now)
        Min = min(Min, now)
        return
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            if i == 0:
                dfs(now+L[cnt], cnt + 1)
            elif i == 1:
                dfs(now-L[cnt], cnt + 1)
            elif i == 2:
                dfs(now*L[cnt], cnt + 1)
            elif i == 3:
                if now * L[cnt] < 0:
                    dfs((abs(now) // abs(L[cnt]) * -1), cnt + 1)
                else:
                    dfs(now//L[cnt], cnt + 1)
            oper[i] += 1


INF = int(1e10)
N = int(input())
L = list(map(int, input().split()))
oper = list(map(int, input().split()))
Max, Min = -INF, INF
dfs(L[0], 1)
print(Max)
print(Min)