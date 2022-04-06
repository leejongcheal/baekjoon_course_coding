from copy import deepcopy
def dfs(now, visit, depth):
    if depth == C:
        res.append((deepcopy(visit)))
        return
    if now >= M - 1:
        return
    for i in range(now, M - 1):
        if visit[i] == 0:
            visit[i] = visit[i+1] = 1
            dfs(i + 2, visit, depth + 1)
            visit[i] = visit[i+1] = 0
def calculate(r):
    s = ""
    i = 0
    while i < M:
        if r[i] == 0:
            if i != M-1:
                s += number[i] + oper[i]
            else:
                s += number[i]
            i += 1
        elif r[i] == 1:
            temp = number[i] + oper[i] + number[i+1]
            s += str(eval(temp))
            if i+1 != M - 1:
                s += oper[i+1]
            i += 2
    return eval(s)



N = int(input())
L = list(input())
oper = [L[i] for i in range(N) if i %2 == 1]
number = [L[i] for i in range(N) if i %2 == 0]
M = len(number)
res = [[0]*M]
cal_max = -1e10
visit = [0]*M
for C in range(1, M//2 + 1):
    dfs(0, visit, 0)
for r in res:
    cal_max = max(cal_max, calculate(r))
print(cal_max)