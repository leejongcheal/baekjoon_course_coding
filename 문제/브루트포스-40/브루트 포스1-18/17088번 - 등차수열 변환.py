from copy import deepcopy
N = int(input())
L = list(map(int, input().split()))
INF = int(1e10)
res = INF
if N <= 2:
    res = 0
else:
    for x in range(-1, 2):
        for y in range(-1, 2):
            oper = 0
            oper += abs(x) + abs(y)
            diff = L[1] + x - L[0] - y
            flag = 0
            temp = deepcopy(L)
            temp[1] += x
            temp[0] += y
            for i in range(2, N):
                if temp[i] - temp[i-1] == diff:
                    continue
                elif temp[i] - temp[i-1] == diff + 1:
                    temp[i] -= 1
                    oper += 1
                elif temp[i] - temp[i-1] == diff - 1:
                    temp[i] += 1
                    oper += 1
                else:
                    flag = 1
                    break
            if flag:
                continue
            res = min(res, oper)
if res == INF:
    print(-1)
else:
    print(res)